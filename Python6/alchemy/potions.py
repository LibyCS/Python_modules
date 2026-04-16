from .elements import create_earth, create_air
from elements import create_fire, create_water


def healing_potion() -> str:
    """
    Uses those functions from this packages element.py
    functions to return a string
    """
    return (f"Healing potion brewed with '{create_earth()}'"
            f" and '{create_air()}'")


def strength_potion() -> str:
    """
    Uses the top level elements.py functions and returns
    a string
    """
    return (f"Strength potion brewed with '{create_fire()}'"
            f" and '{create_water()}'")
