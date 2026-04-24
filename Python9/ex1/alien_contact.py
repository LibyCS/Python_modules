from pydantic import BaseModel, Field, ValidationError
from pydantic import model_validator  # type: ignore[attr-defined]
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """
    Class which inherits the pydantic model
    and creates fields with types and requirements
    """
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: (str | None) = Field(max_length=500, default=None)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate(self) -> "AlienContact":
        """
        Custom validator rules for the fields above
        """
        if self.contact_id[:2] != "AC":
            raise ValueError("Contact ID must start with \"AC\"")
        if not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least"
                             " 3 witnesses")
        if self.signal_strength < 7.0:
            raise ValueError("Strong signals (> 7.0) should include"
                             " received messages")
        return self


def format(ac: AlienContact) -> None:
    labels = {"contact_id": "ID", "timestamp": "Date", "location": "Location",
              "contact_type": "Type", "signal_strength": "Signal",
              "duration_minutes": "Duration", "witness_count": "Witnesses",
              "message_received": "Message", "is_verified": "Verified"}
    for key, value in ac.__dict__.items():
        if (key != "message_received" and key != "is_verified"
           and key != "contact_type"):
            print(f"{labels[key]}: {value}", end="")
        elif key == "contact_type":
            print(f"{labels[key]}: {value.value}", end="")
        elif key == "message_received" and value:
            print(f"{labels[key]}: '{value}'", end="")
        if key == "signal_strength":
            print("/10", end="")
        elif key == "duration_minutes":
            print(" minutes", end="")
        if value and key != "is_verified":
            print("")


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    ac = AlienContact(contact_id="AC_2024_001", timestamp=datetime.today(),
                      contact_type=ContactType.RADIO,
                      location="Area 51, Nevada", signal_strength=8.5,
                      duration_minutes=45, witness_count=5,
                      message_received="Greetings from Zeta Reticuli",
                      is_verified=True)
    format(ac)
    print("\n======================================")
    print("Expected validation error:")
    try:
        ac = AlienContact(contact_id="AC_2024_001", timestamp=datetime.today(),
                          contact_type=ContactType.RADIO,
                          location="Area 51, Nevada", signal_strength=8.5,
                          duration_minutes=45, witness_count=1,
                          message_received="",
                          is_verified=True)
        format(ac)
    except ValidationError as error:
        for message in error.errors():
            if "Value error, " in message["msg"]:
                index = message["msg"].find(", ")
                print(message["msg"][index + 2:])
            else:
                print(message["msg"])


if __name__ == "__main__":
    main()
#    import json
#    import csv
#    from alien_contacts import ALIEN_CONTACTS as data
#    with open("alien_contacts.csv") as f:
#        json.load()
#        csv.DictReader()
#        data = csv.DictReader(f)
#    try:
#        for items in data:
#            format(AlienContact(**items))
#    except ValidationError as error:
#        for message in error.errors():
#            print(message["msg"])
