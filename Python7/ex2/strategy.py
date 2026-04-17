from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import HealingCapability, TransformCapability


class BattleStrategy(ABC):
    def __init__(self) -> None:
        self.name: (str | None) = None

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """
        First checks if the creature is valid
        then perfroms the actions
        """
        if isinstance(self.name, str):
            name = self.name.lower()
        if not self.is_valid(creature):
            raise AttributeError("Battle error, aborting tournament:"
                                 f" Invalid creature '{creature.name}' for"
                                 f" this {name} strategy")

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """
        Checks if the creature has the methods required,
        returns True or False
        """
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Normal"

    def act(self, creature: Creature) -> None:
        """
        First checks if the creature is valid
        then perfroms the actions
        """
        super().act(creature)
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        """
        Checks if the creature has the methods required,
        returns True or False
        """
        if creature.attack():
            return True
        return False


class AgressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Aggressive"

    def act(self, creature: Creature) -> None:
        """
        First checks if the creature is valid
        then perfroms the actions
        """
        super().act(creature)
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())

    def is_valid(self, creature: Creature) -> bool:
        """
        Checks if the creature has the methods required,
        returns True or False
        """
        if (isinstance(creature, TransformCapability) and creature.transform()
                and creature.revert() and creature.attack()):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Defensive"

    def act(self, creature: Creature) -> None:
        """
        First checks if the creature is valid
        then perfroms the actions
        """
        super().act(creature)
        if isinstance(creature, HealingCapability):
            print(creature.attack())
            print(creature.heal())

    def is_valid(self, creature: Creature) -> bool:
        """
        Checks if the creature has the methods required,
        returns True or False
        """
        if (isinstance(creature, HealingCapability) and creature.heal()
                and creature.attack()):
            return True
        return False
