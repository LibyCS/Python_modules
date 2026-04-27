import functools
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    depending on the operator we return 1 single value
    using reduce.
    """
    if not spells:
        return 0
    if operation == "add":
        return functools.reduce(operator.add, spells)
    elif operation == "multiply":
        return functools.reduce(operator.mul, spells)
    elif operation == "max":
        return functools.reduce(max, spells)
    elif operation == "min":
        return functools.reduce(min, spells)
    else:
        raise ValueError("Invalid operator was given")


def enchantment(power: int, element: str, target: str) -> str:
    """
    returns fully formatted string
    """
    return f"Used the element {element} to hit {target} for {power} damage"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """
    partially formats the function using partial, only sets
    power and element, not the target
    """
    fire = functools.partial(base_enchantment, 50, "fire")
    water = functools.partial(base_enchantment, 50, "water")
    earth = functools.partial(base_enchantment, 50, "earth")
    return {"fire": fire, "water": water, "earth": earth}


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    """
    remembers the pervious arguments and results parsed
    through, quicker run time, less computations needed as
    it retrieves cache results instead if the same
    """
    num = 0
    if n == 1:
        num = 1
    elif n >= 2:
        num = memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
    return num


def spell_dispatcher() -> Callable[[Any], str]:
    """
    returns the function dispatch which depending on the tpye
    of the argument will be sent to a corrosponding function
    created
    """
    @functools.singledispatch
    def dispatcher(spell_type: Any) -> str:
        """
        returns unknwon if it doesnt have the correct type
        """
        return "Unknown spell type"

    @dispatcher.register
    def _(dmg: int) -> str:
        """
        for int data
        """
        return f"Damage spell: {dmg} damage"

    @dispatcher.register
    def _(enchant: str) -> str:
        """
        for str data
        """
        return f"Enchantment: {enchant}"

    @dispatcher.register
    def _(multi: list) -> str:
        """
        for list data
        """
        return f"Multi-cast: {len(multi)} spells"
    return dispatcher


if __name__ == "__main__":
    print("Testing spell reducer...")
    spell_power = [40, 30, 20, 10]
    try:
        print("Sum:", spell_reducer(spell_power, "add"))
        print("Product:", spell_reducer(spell_power, "multiply"))
        print("Max:", spell_reducer(spell_power, "max"))
        print("Min:", spell_reducer(spell_power, "min"))
        print("Unknown:", spell_reducer(spell_power, "unknown"))
    except ValueError as message:
        print(message)
    print("\nTesting partial enchanter...")
    enchanter = partial_enchanter(enchantment)
    print(enchanter["fire"]("Dragon"))
    print(enchanter["water"]("Dragon"))
    print(enchanter["earth"]("Dragon"))
    print("\nTesting memoized fibonacci...")
    fib = [0, 1, 10, 15]
    for i in fib:
        print(f"Fib({i}):", memoized_fibonacci(i))
    print("First run cache info:")
    print(memoized_fibonacci.cache_info())
    for i in fib:
        memoized_fibonacci(i)
    print("Second run cache info:")
    print(memoized_fibonacci.cache_info())
    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["frizz", "crack", "whoosh"]))
    print(dispatcher(53.5))
