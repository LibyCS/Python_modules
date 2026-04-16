from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1 import HealingCapability, TransformCapability
from ex0 import CreatureFactory


def factory(fac: CreatureFactory):
    """
    Checks if the factory functions are valid
    then uses the factory function to show off
    base and evolved creatures
    """
    if not fac.create_base() or not fac.create_evolved():
        print("Error: Invalid factory without the valid functions passed")
    creatures = [fac.create_base(), fac.create_evolved()]
    for creature in creatures:
        if creature == creatures[0]:
            print(" base:")
        else:
            print(" evolved:")
        print(f"{creature.describe()}\n{creature.attack()}")
        if isinstance(creature, HealingCapability):
            print(creature.heal())
        elif isinstance(creature, TransformCapability):
            print(f"{creature.transform()}\n{creature.attack()}")
            print(creature.revert())


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    healing = HealingCreatureFactory()
    factory(healing)
    print("\nTesting creature with transform capability")
    transforming = TransformCreatureFactory()
    factory(transforming)
