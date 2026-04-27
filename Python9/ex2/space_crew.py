from pydantic import BaseModel, Field, ValidationError
from pydantic import model_validator  # type: ignore[attr-defined]
from enum import Enum
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialisation: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation(self) -> "SpaceMission":
        if self.mission_id[0] != "M":
            raise ValueError("Mission ID must start with 'M'")
        supervisor = False
        for member in self.crew:
            if member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN:
                supervisor = True
            if member.is_active is False:
                raise ValueError("All crew members must be active")
        if supervisor is False:
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            experienced = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced += 1
            if experienced < (len(self.crew) / 2):
                raise ValueError("Long missions (> 365 days) need 50%"
                                 " experienced crew (5+ years)")
        return self


def format(mission: SpaceMission) -> None:
    print("Valid mission created:")
    labels = {"mission_name": "Mission", "mission_id": "ID",
              "destination": "Destination", "launch_date": "Launch",
              "duration_days": "Duration", "crew": "Crew",
              "mission_status": "Status", "budget_millions": "Budget"}
    print(f"Mission: {mission.mission_name}")
    for key, value in mission.__dict__.items():
        if (key != "crew" and key != "mission_status"
           and key != "budget_millions" and key != "launch_date"
           and key != "mission_name"):
            print(f"{labels[key]}: {value}")
        elif key == "crew":
            print(f"Budget: ${mission.budget_millions}M")
            print(f"Crew size: {len(value)}")
            print("Crew members:")
            for member in mission.crew:
                print(f"- {member.name} ({member.rank.value}) -"
                      f" {member.specialisation}")


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        crew1 = CrewMember(member_id="CM001", name="Sarah Williams",
                           rank=Rank.CAPTAIN, age=43,
                           specialisation="Mission Command",
                           years_experience=19, is_active=True)
    except ValidationError as error:
        print("Crew member could not be parsed")
        for message in error.errors():
            print(message["msg"])
    try:
        crew2 = CrewMember(member_id="CM002", name="James Hernandez",
                           rank=Rank.LIEUTENANT, age=43,
                           specialisation="pilot",
                           years_experience=30, is_active=True)
    except ValidationError as error:
        print("Crew member could not be parsed")
        for message in error.errors():
            print(message["msg"])
    try:
        crew3 = CrewMember(member_id="CM003", name="Anna Jones",
                           rank=Rank.CADET, age=35,
                           specialisation="communications",
                           years_experience=15, is_active=True)
    except ValidationError as error:
        print("Crew member could not be parsed")
        for message in error.errors():
            print(message["msg"])
    try:
        crew4 = CrewMember(member_id="CM004", name="David Smith",
                           rank=Rank.OFFICER, age=27,
                           specialisation="communications",
                           years_experience=15, is_active=True)
    except ValidationError as error:
        print("Crew member could not be parsed")
        for message in error.errors():
            print(message["msg"])
        return
    mission = SpaceMission(mission_id="M2024_MARS",
                           mission_name="Mars Colony Establishment",
                           destination="Mars",
                           launch_date=datetime.fromisoformat("2026-04-24"),
                           duration_days=900,
                           crew=[crew1, crew2, crew3],
                           budget_millions=2500.0)
    format(mission)
    print("\n=========================================")
    print("Expected validation error:")
    try:
        miss2 = SpaceMission(mission_id="M2024_MARS",
                             mission_name="Mars Colony Establishment",
                             destination="Mars",
                             launch_date=datetime.fromisoformat("2024-04-24"),
                             duration_days=900,
                             crew=[crew2, crew3, crew4],
                             budget_millions=2500.0)
        format(miss2)
    except ValidationError as error:
        for message in error.errors():
            if "Value error, " in message["msg"]:
                index = message["msg"].find(", ")
                print(message["msg"][index + 2:])
            else:
                print(message["msg"])


if __name__ == "__main__":
    main()
