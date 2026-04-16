from ex0 import Creature
from .capability import HealingCapability, TransformCapability


class Sproutling(Creature, HealingCapability):
    """
    A capable creature with added healing abilities
    """
    def __init__(self) -> None:
        """
        Inherits the init from Creature,
        HealingCapability has no init
        """
        super().__init__()
        self.name = "Sproutling"
        self.type = "Grass"

    def attack(self) -> str:
        """
        Returns a string specific for this creature
        """
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: (Creature | None) = None) -> str:
        """
        Checks weather there is a target to heal
        if not heals itself, returns that string
        """
        if not target:
            return f"{self.name} heals itself for a small amount"
        return f"{self.name} heals {target.name} for a small amount"


class Bloomelle(Creature, HealingCapability):
    """
    A capable creature with added healing abilities
    """
    def __init__(self) -> None:
        """
        Inherits the init from Creature,
        HealingCapability has no init
        """
        super().__init__()
        self.name = "Bloomelle"
        self.type = "Grass/Fairy"

    def attack(self) -> str:
        """
        Returns a string specific for this creature
        """
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: (Creature | None) = None) -> str:
        """
        Doesnt care if there is a target or not it heals everything
        """
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    """
    A capable creature with Transformation abilities
    """
    def __init__(self) -> None:
        """
        Needs to inherit both parents init variables
        """
        Creature.__init__(self)
        TransformCapability.__init__(self)
        self.name = "Shiftling"
        self.type = "Normal"

    def attack(self) -> str:
        """
        Returns string of attack
        """
        if self.state is False:
            return f"{self.name} attacks normally."
        return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        """
        Transforms the creature into a strong form
        """
        if self.state is True:
            return "Already transformed, cannot transform any further"
        self.state = True
        return f"{self.name} shifts into a sharper form"

    def revert(self) -> str:
        """
        Reverts back to the original form
        """
        if self.state is False:
            return "Already in original form, cannot revert any further"
        self.state = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    """
    A capable creature with Transformation abilities
    """
    def __init__(self) -> None:
        """
        Needs to inherit both parents init variables
        """
        Creature.__init__(self)
        TransformCapability.__init__(self)
        self.name = "Morphagon"
        self.type = "Normal/Dragon"

    def attack(self) -> str:
        """
        Returns string of attack
        """
        if self.state is False:
            return f"{self.name} attacks normally."
        return f"{self.name} unleashes a devestating morph strike!"

    def transform(self) -> str:
        """
        Transforms the creature into a strong form
        """
        if self.state is True:
            return "Already transformed, cannot transform any further"
        self.state = True
        return f"{self.name} morphs into a dragonic battle form"

    def revert(self) -> str:
        """
        Reverts back to the original form
        """
        if self.state is False:
            return "Already in original form, cannot revert any further"
        self.state = False
        return f"{self.name} stabalises its form."
