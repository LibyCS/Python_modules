from abc import ABC, abstractmethod
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    """
    Template for the child factory classes to use
    """
    @abstractmethod
    def create_base(self) -> Creature:
        """
        Returns an instance of the base creature
        must be edited by child
        """
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """
        returns an instance of the evolved creature
        must be edited by child
        """
        pass


class FlameFactory(CreatureFactory):
    """
    Inherits template from CreatureFactory
    """
    def create_base(self) -> Creature:
        """
        Returns instance of base creature Flameling
        """
        return Flameling()

    def create_evolved(self) -> Creature:
        """
        Returns instance of evolved creature Pyrodon
        """
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """
    Inherits template from CreatureFactory
    """
    def create_base(self) -> Creature:
        """
        Returns instance of base creature Aquabub
        """
        return Aquabub()

    def create_evolved(self) -> Creature:
        """
        Returns instance of evolved creature Torragon
        """
        return Torragon()
