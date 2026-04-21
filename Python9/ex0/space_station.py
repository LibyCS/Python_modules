from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    """
    A pydantic model where you can initialise,
    validate and convert the value into its given
    type.
    Field is the valid parameters
    """
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: (str | None) = Field(max_length=200, default=None)


def format(spacestation: SpaceStation) -> None:
    """
    prints the space station fields as formatted in
    a clear and unnderstandable way
    """
    labels = {"station_id": "ID", "name": "Name", "crew_size": "Crew",
              "power_level": "Power", "oxygen_level": "Oxygen",
              "last_maintenance": "Last Maintenance",
              "is_operational": "Status", "notes": "Notes"}
    for key, value in spacestation.__dict__.items():
        if key == "last_maintenance" or (key == "notes" and not value):
            continue
        print(f"{labels[key]}: ", end="")
        if key != "is_operational":
            print(value, end="")
        else:
            if value is True:
                print("Operational", end="")
            else:
                print("Not Operational", end="")
        if key == "crew_size":
            print(" people", end="")
        elif key == "power_level" or key == "oxygen_level":
            print("%", end="")
        print()


def main() -> None:
    """
    Main function that initialises the pydatantic model
    and tests with valid and invalid fields
    """
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    spacestation = SpaceStation(station_id="ISS001",
                                name="International Space Station",
                                crew_size=6, power_level=85.5,
                                oxygen_level=92.3,
                                last_maintenance=datetime.today())
    format(spacestation)
    print("\n========================================")
    print("Expected validation error:")
    try:
        last_date = datetime.fromisoformat("2026-04-20")
        spacestation = SpaceStation(station_id="ISS001",
                                    name="International Space Station",
                                    crew_size=200, power_level=85.5,
                                    oxygen_level=92.3,
                                    last_maintenance=last_date,
                                    is_operational=False)
        format(spacestation)
    except ValidationError as error:
        for message in error.errors():
            print(message["msg"])


if __name__ == "__main__":
    main()
