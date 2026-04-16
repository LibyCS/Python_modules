from abc import ABC, abstractmethod


class Creature(ABC):
    """
    Abstract class that will set the template
    for all creatures that inherit from it
    """
    def __init__(self) -> None:
        """
        Sets attributes for all
        classes which inherit creature
        """
        self.name: (str | None) = None
        self.type: (str | None) = None

    @abstractmethod
    def attack(self) -> str:
        """
        Abstract method that must be edited by
        the children classes
        """
        pass

    def describe(self) -> str:
        """
        Returns a string about the object
        """
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    """
    Flameling that inherits from Creature
    """
    def __init__(self) -> None:
        """
        Sets attributes that are appropriate for this child
        class
        """
        super().__init__()
        self.name = "Flameling"
        self.type = "Fire"

    def attack(self) -> str:
        """
        Returns a string descibing the attack
        """
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    """
    Pyrodon that inherits from Creature
    """
    def __init__(self) -> None:
        """
        Sets attributes that are appropriate for this child
        class
        """
        super().__init__()
        self.name = "Pyrodon"
        self.type = "Fire/Flying"

    def attack(self) -> str:
        """
        Returns a string descibing the attack
        """
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    """
    Aquabub that inherits from Creature
    """
    def __init__(self) -> None:
        """
        Sets attributes that are appropriate for this child
        class
        """
        super().__init__()
        self.name = "Aquabub"
        self.type = "Water"

    def attack(self) -> str:
        """
        Returns a string descibing the attack
        """
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    """
    Torragon that inherits from Creature
    """
    def __init__(self) -> None:
        """
        Sets attributes that are appropriate for this child
        class
        """
        super().__init__()
        self.name = "Torragon"
        self.type = "Water"

    def attack(self) -> str:
        """
        Returns a string descibing the attack
        """
        return f"{self.name} uses Hydro Pump!"


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
