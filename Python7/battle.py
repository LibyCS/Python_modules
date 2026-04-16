from ex0 import CreatureFactory, FlameFactory, AquaFactory


def factory(fac: CreatureFactory) -> None:
    if not fac.create_base() or not fac.create_evolved():
        print("Error: Factory does not have the valid functions needed")
        return
    base = fac.create_base()
    print(f"{base.describe()}\n{base.attack()}")
    evolved = fac.create_evolved()
    print(f"{evolved.describe()}\n{evolved.attack()}")


def battle(fac1: CreatureFactory, fac2: CreatureFactory) -> None:
    if not fac1.create_base() or not fac2.create_base():
        print("Error: Factory does not have the valid functions needed")
        return
    base1 = fac1.create_base()
    base2 = fac2.create_base()
    print(f"{base1.describe()}\n vs.\n{base2.describe()}\n fight!")
    print(f"{base1.attack()}\n{base2.attack()}")


if __name__ == "__main__":
    print("Testing Factory")
    factory(FlameFactory())
    print()
    factory(AquaFactory())
    print("\nTesting battle")
    battle(FlameFactory(), AquaFactory())
