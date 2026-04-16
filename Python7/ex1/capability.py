from abc import ABC, abstractmethod
from ex0 import Creature


class HealingCapability(ABC):
    """
    HealingCapability template, all children
    will inherit heal that must be edited
    """
    @abstractmethod
    def heal(self, target: (Creature | None) = None) -> str:
        pass


class TransformCapability(ABC):
    """
    Transform template, all children will inherit transform
    and rever functions that must be eddited
    """
    def __init__(self):
        """
        Keeps track what state the creature is in
        """
        self.state = False

    @abstractmethod
    def transform(self) -> str:
        """
        sets the state to true meaning the creature is transformed
        """
        pass

    @abstractmethod
    def revert(self) -> str:
        """
        Sets the state to false meaning the creature has reverted
        """
        pass
