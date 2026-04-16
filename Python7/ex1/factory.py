from ex0 import CreatureFactory, Creature
from .creature import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    """
    Factory to create base and evolved forms of the capable creatures
    """
    def create_base(self) -> Creature:
        """
        Returns an instance of the base version
        """
        return Sproutling()

    def create_evolved(self) -> Creature:
        """
        Returns an instance of the evolved version
        """
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """
    Factory to create base and evolved forms of the capable creatures
    """
    def create_base(self) -> Creature:
        """
        Returns an instance of the base version
        """
        return Shiftling()

    def create_evolved(self) -> Creature:
        """
        Returns an instance of the evolved version
        """
        return Morphagon()
