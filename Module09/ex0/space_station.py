#!/usr/bin/env python3

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10,
                            description="Id of the space station")
    name: str = Field(..., min_length=1, max_length=50,
                      description="Full name of the space station")
    crew_size: int = Field(..., ge=1, le=20, description="Size of the crew")
    power_level: float = Field(..., ge=0.0, le=100.0,
                               description="Percentage of power on the "
                               "station")
    oxygen_level: float = Field(..., ge=0.0, le=100.0,
                                description="Percentage of oxygen on the "
                                "station")
    last_maintenance: datetime = Field(..., description="Date of the last "
                                       "maintenance did")
    is_operational: bool = Field(default=True, description="True of False if "
                                 "the station is operational")
    notes: Optional[str] = Field(max_length=200, description="Optional notes")


if __name__ == "__main__":
    try:

        print("Space Station Data Validation"
              "========================================")

        station = SpaceStation(
            station_id="ATS",
            name="Above The Sky",
            crew_size=6,
            power_level=79.4,
            oxygen_level=83.7,
            last_maintenance="2026-5-30T14:54:15",
            notes=None
        )

        print(
            "Valid station created:\n"
            f"ID: {station.station_id}\n"
            f"Name: {station.name}\n"
            f"Crew: {station.crew_size} people\n"
            f"Power: {station.power_level}%\n"
            f"Oxygen: {station.oxygen_level}%\n"
            "Status: "
            f"{'Operational' if station.is_operational
               else 'Not operational'}"
        )
        if station.notes:
            print(f"Note: {station.notes}")
        print("========================================\n"
              "Expected validation error:")
        station = SpaceStation(
            station_id="ATS",
            name="Above The Sky",
            crew_size=21,
            power_level=79.4,
            oxygen_level=83.7,
            last_maintenance="2026-5-30T14:54:45",
            notes=None
        )
    except Exception as err:
        print(err)
