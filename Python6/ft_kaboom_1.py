if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now- THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    try:
        import alchemy.grimoire.dark_spellbook as dark
        print("Testing record dark spell: "
              f"{dark.dark_spell_record("Fanatsy", "Earth, bats and fire")}")
    except ImportError:
        print("ImportError: Unable to import dark_spell_allowed_ingredients"
              " due to circular import")
