from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """
    Returns a list of allowed ingredients
    """
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """
    Determines if the spell is valid by comparing the
    ingredients given vs the valid ingreduents
    """
    validate: str = validate_ingredients(ingredients)
    if "INVALID" not in validate:
        return f"Spell recorded: {spell_name} {validate}"
    return f"Spell rejected: {spell_name} {validate}"
