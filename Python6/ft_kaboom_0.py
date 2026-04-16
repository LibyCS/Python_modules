import alchemy.grimoire as grim

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print("Testing record light spell: "
          f"{grim.light_spell_record("Fanatsy", "Earth, wind and fire")}")
    print("Testing record light spell: "
          f"{grim.light_spell_record("Fanatsy", "dark, wind and light")}")
