from typing import Callable, Any


def mage_counter() -> Callable[[], int]:
    """
    Returns a function that counts how many times it gets called
    """
    counted: int = 0

    def counter() -> int:
        """
        Uses counted variable from above and adds 1
        everytime it is called
        """
        nonlocal counted
        counted += 1
        return counted
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """
    Returns a function that accumulates power over time
    """
    power: int = initial_power

    def total_power(added_power: int) -> int:
        """
        Takes in an additional power param to add
        to the total power, and keeps track
        """
        nonlocal power
        power += added_power
        return power
    return total_power


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """
    creates enchantment functions where the the retuurned
    function applies specified enchantment
    """

    def enchanted(item_name: str) -> str:
        """
        Uses enchantment_type from the outer function when the inner
        enchanted function object is created, and takes item name
        form function object to return a description
        """
        return f"{enchantment_type} {item_name}"
    return enchanted


def memory_vault() -> dict[str, Callable[..., Any]]:
    """
    returns a dictionary function of store and recall
    """
    memory = {}

    def store(key: str, value: int) -> None:
        """
        Stores key value in a dictionary in the outer
        function
        """
        nonlocal memory
        memory[key] = value

    def recall(key: str) -> (int | str):
        """
        Checks if the key exists and returns the
        corrosponding value
        """
        if key in memory.keys():
            return memory[key]
        return "Memory not found"
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    for i in range(2):
        print(f"counter_a call {i}: {counter_a()}")
    print("counter_b call 1:", counter_b())
    print("\nTesting spell accumulator...")
    accumulation = spell_accumulator(100)
    power = [20, 30]
    for i in power:
        print(f"Base 100, add {i}: {accumulation(i)}")
    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("sword"))
    print(frozen("shield"))
    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault["recall"]("secret")}")
    print(f"Recall 'unknown': {vault["recall"]("unknown")}")
