#!/usr/bin/env pyhton3

from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from typing import List


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10,
                           description="Id of the crew member")
    name: str = Field(..., min_length=2, max_length=50,
                      description="Full name of the crew member")
    rank: Rank = Field(...)
    age: int = Field(ge=18, le=80, description="Age of the crew member")
    specialization: str = Field(..., min_length=3, max_length=30,
                                description="Specialization of crew member")
    years_experience: int = Field(
        ..., ge=0, le=50, description="Crew member's years of experience")
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15,
                            description="ID of the mission")
    mission_name: str = Field(..., min_length=3, max_length=100,
                              description="Full name of the mission")
    destination: str = Field(..., min_length=3, max_length=50,
                             description="Destination of the mission")
    launch_date: datetime = Field(...,
                                  description="Date and time of the mission")
    duration_days: int = Field(..., ge=1, le=3650,
                               description="Duration of the mission in days")
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12,
                                   description="List of crew members")
    mission_status: str = Field(default="planned",
                                description="Current status of the mission")
    budget_millions: float = Field(
        ..., ge=1.0, le=10000.0,
        description="Budget for the mission in million dolars")

    @model_validator(mode="after")
    def validate(self) -> "SpaceMission":
        if not self.mission_id[0] == "M":
            raise ValueError("Mission ID must start with 'M'")
        captain_commander = False
        experienced = 0
        for person in self.crew:
            if not person.is_active:
                raise ValueError(f"{person.name} isn't a active crew member")
            if person.rank in [Rank.commander, Rank.captain]:
                captain_commander = True
            if person.years_experience >= 5:
                experienced += 1
        if not captain_commander:
            raise ValueError(
                "Mission must have at least one Commander or Captain")
        if experienced < len(self.crew) / 2 and self.duration_days > 365:
            raise ValueError("Need at least 50% of the crew with more than 5 "
                             "years of experience for a long mission. "
                             f"Currently {experienced}/{len(self.crew)} are.")
        return self


if __name__ == "__main__":
    def print_mission_data(mission: SpaceMission) -> None:
        print(f"Mission: {mission.mission_name}\n"
              f"ID: {mission.mission_id}\n"
              f"Destination: {mission.destination}\n"
              f"Duration: {mission.duration_days} days\n"
              f"Budget: ${mission.budget_millions:.1f}M\n"
              f"Crew size: {len(mission.crew)}\n"
              "Crew members:")
        for person in mission.crew:
            print(f"- {person.name} ({person.rank.value}) - "
                  f"{person.specialization}")

    try:
        from data_generator import CrewMissionGenerator, DataConfig
    except Exception as err:
        print(f"Importing data generation module: {err}")
        exit(1)

    try:
        print("Space Mission Crew Validation\n"
              "=========================================")
        generator = CrewMissionGenerator(DataConfig(11, datetime(2026, 6, 15)))
        missions = generator.generate_mission_data(3)
        for mission in missions:
            current = SpaceMission(
                mission_id=mission["mission_id"],
                mission_name=mission["mission_name"],
                destination=mission["destination"],
                launch_date=mission["launch_date"],
                duration_days=mission["duration_days"],
                budget_millions=mission["budget_millions"],
                crew=[CrewMember(
                    member_id=each["member_id"],
                    name=each["name"],
                    rank=each["rank"],
                    age=each["age"],
                    specialization=each["specialization"],
                    years_experience=each["years_experience"],
                    is_active=each["is_active"]
                ) for each in mission["crew"]]
            )
            print_mission_data(current)
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

        print("\n=========================================\n"
              "Expected validation error:")
        mission_fail = SpaceMission(
            mission_id="N_FAIL",
            mission_name="Mission Fail",
            destination="Nebula",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500.3,
            crew=[
                CrewMember(
                    member_id="SCN",
                    name="Sarah Connor",
                    rank="officer",
                    age=55,
                    specialization="Cleaning",
                    years_experience=35,
                    is_active=False
                ),
                CrewMember(
                    member_id="JSM",
                    name="John Smith",
                    rank="lieutenant",
                    age=40,
                    specialization="Navigation",
                    years_experience=4
                ),
                CrewMember(
                    member_id="AJH",
                    name="Alice Johnson",
                    rank="officer",
                    age=30,
                    specialization="Engineering",
                    years_experience=4
                )
            ]
        )
        print_mission_data(mission_fail)

    except ValidationError as err:
        print(err.errors()[0]["msg"].split(",")[1].strip())
    except Exception as err:
        print(err)
