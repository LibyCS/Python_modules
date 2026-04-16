from .. import create_air, strength_potion
from elements import create_fire


def lead_to_gold() -> str:
    """
    Returns a string using the previous functions exposed
    by alchemy or from the top level elements.
    """
    return (f"Recipe transmutating Lead to Gold: brew '{create_air()}'"
            f" and '{strength_potion()}' mixed with '{create_fire()}'")
