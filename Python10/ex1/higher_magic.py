from typing import Callable


def fireball(target: str, power: int) -> str:
    """
    Spell that returns a string
    """
    return f"Fireball hits {target} for {power} damage"


def crack(target: str, power: int) -> str:
    """
    Spell that returns a string
    """
    return f"Crack hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    """
    Spell that returns a string
    """
    return f"Heal restores {target} for {power} HP"


def conditions(target: str, power: int) -> bool:
    if power >= 50:
        return True
    return False


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """
    Takes in 2 functions and combines them
    with unknown args, runs them through both
    callable functions and returns the output in a tuple
    """
    def combined(*args) -> tuple[str, str]:
        return (spell1(*args), spell2(*args))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """
    Has 2 callable functions that are parsed through, we set the
    first 2 args as target and power so we can manipulate them
    in base_spell
    """
    def amplified(*args) -> str:
        """
        takes the first 2 args and inputs them in base_spell
        while modifying power
        """
        target, power = args
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """
    Spell only passes if the condition returns true, this returns
    conditioned function
    """
    def conditioned(*args) -> str:
        """
        Checks if condition is true then runs spell
        if not returns spell fizzled
        """
        if condition(*args):
            return spell(*args)
        return "Spell fizzled"
    return conditioned


def spell_sequence(spells: list[Callable]) -> Callable:
    """
    takes in a list of functions all with the same arguments
    casts each spell in order
    """
    def all_spells(*args) -> list[str]:
        """
        Goes through each spell function, runs them and appends
        to a string
        """
        return list(map(lambda spell: spell(*args), spells))
    return all_spells


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    try:
        print(combined("Dragon", 50))
    except TypeError:
        print("Arguments are incorrect")
    print("Testing power amplifier...")
    try:
        amplified = power_amplifier(fireball, 2)
        print(amplified("Dragon", 50))
    except TypeError:
        print("Arguments are incorrect")
    print("Testing conditionals...")
    print("Testing true:")
    conditioned = conditional_caster(conditions, fireball)
    try:
        print(conditioned("Dragon", 50))
    except TypeError:
        print("Arguments are incorrect")
    print("Testing false:")
    try:
        print(conditioned("Dragon", 20))
    except TypeError:
        print("Arguments are incorrect")
    print("Testing sequence of spells...")
    all_spells = spell_sequence([fireball, crack, heal])
    try:
        print(all_spells("Dragon", 50))
    except TypeError:
        print("Arguments are incorrect")
