def validate_ingredients(ingredients: str) -> str:
    """
    Compares the ingredients if its valid
    and returns the ingredients plus
    VALID or INVALID
    """
    from .light_spellbook import light_spell_allowed_ingredients
    for ingredient in light_spell_allowed_ingredients():
        if ingredient in ingredients.lower():
            return "(" + ingredients + " - VALID" + ")"
    return "(" + ingredients + " - INVALID" + ")"
