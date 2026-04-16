from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """
    Compares the ingredients if its valid
    and returns the ingredients plus
    VALID or INVALID
    """
    for ingredient in dark_spell_allowed_ingredients():
        if ingredient in ingredients.lower():
            return "(" + ingredients + " - VALID" + ")"
    return "(" + ingredients + " - INVALID" + ")"
