def light_spell_allowed_ingredients() -> list[str]:
    """
    Returns a list of allowed ingredients
    """
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """
    Determines if the spell is valid by comparing the
    ingredients given vs the valid ingreduents
    """
    from .light_validator import validate_ingredients
    validate: str = validate_ingredients(ingredients)
    if "INVALID" not in validate:
        return f"Spell recorded: {spell_name} {validate}"
    return f"Spell rejected: {spell_name} {validate}"
