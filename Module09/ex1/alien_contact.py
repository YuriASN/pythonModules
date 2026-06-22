#!/usr/bin/env python3

from pydantic import BaseModel, model_validator, Field, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15,
                            description="Contact id must start with AC")
    timestamp: datetime = Field(..., description="Date and time of contact")
    location: str = Field(..., min_length=3, max_length=100,
                          description="Location of contact")
    contact_type: ContactType = Field(
        ..., description="Form of contact ContactType enum")
    signal_strength: float = Field(..., ge=0.0, le=10.0,
                                   description="Strength of the signal")
    duration_minutes: int = Field(..., ge=1, le=1440,
                                  description="Duration of contact in minutes")
    witness_count: int = Field(..., ge=1, le=100,
                               description="Amount of witness")
    message_received: Optional[str] = Field(
        max_length=500, description="Message received during contact")
    is_verified: bool = Field(default=False,
                              description="Contact verification")

    @model_validator(mode="after")
    def validate_id(self) -> "AlienContact":
        if not self.contact_id[:2] == "AC":
            raise ValueError("Contact ID has to start with 'AC'")
        return self

    @model_validator(mode="after")
    def validate_type(self) -> "AlienContact":
        if self.contact_type == ContactType.physical:
            if not self.is_verified:
                raise ValueError("Physical contact has to be validated")
        elif self.contact_type == ContactType.telepathic:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses")
        return self

    @model_validator(mode="after")
    def validate_signal(self) -> "AlienContact":
        if self.signal_strength > 7.0:
            if not self.message_received or not len(self.message_received):
                raise ValueError("Signals stronger than 7.0 "
                                 "should include a received message")
        return self


if __name__ == "__main__":
    def print_contact(contact: AlienContact) -> None:
        try:
            print(f"ID: {contact.contact_id}\n"
                  f"Type: {contact.contact_type.value}\n"
                  f"Location: {contact.location}\n"
                  f"Signal: {contact.signal_strength}/10\n"
                  f"Duration: {contact.duration_minutes} minutes\n"
                  f"Witness: {contact.witness_count}")
            if contact.message_received and len(contact.message_received):
                print(f"Message: '{contact.message_received}'")
        except Exception as err:
            raise Exception(f"Printing contact: {err}")

    try:
        print("Alien Contact Log Validation\n"
              "======================================")
        print("Valid contact report:")
        valid_contact = AlienContact(
            contact_id="AC_Alien_42",
            timestamp="2026-06-07T11:54:15",  # type: ignore[arg-type]
            location="Lisbon, Portugal",
            contact_type="radio",  # type: ignore[arg-type]
            signal_strength=8.5,
            duration_minutes=47,
            witness_count=5,
            message_received="I'm here in peace!"
        )
        print_contact(valid_contact)

        print("\n======================================")
        print("Expected validation error:")
        invalid_contact = AlienContact(
            contact_id="AC_Alien_42",
            timestamp="2026-06-07T11:54:15",  # type: ignore[arg-type]
            location="Lisbon, Portugal",
            contact_type="telepathic",  # type: ignore[arg-type]
            signal_strength=8.5,
            duration_minutes=47,
            witness_count=2,
            message_received="I'm here in peace!"
        )
        print_contact(invalid_contact)
    except ValidationError as err:
        print(err.errors()[0]["msg"].split(",")[1].strip())
    except Exception as err:
        print(err)
