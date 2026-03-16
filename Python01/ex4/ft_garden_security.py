
class Plant:
    """
    a class that gives general structure of
    a plant
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        initialises a plant object with name
        height and age
        """
        self.name = name
        print(f"Plant created: {name}")
        self._height = None
        self.set_height(height)
        self._age = None
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """
        updates height with this method
        checks if its valid
        """
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print("Invalid operation attempted:"
                  f" height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        """
        sets age with this method, checks if the
        age is valid first
        """
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print("Invalid operation attempted:"
                  f" age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> None:
        """
        printd height info
        """
        print(f"{self.name} height is {self._height}cm")

    def get_age(self) -> None:
        """
        prints age info
        """
        print(f"{self.name} age is {self._age} days")


if __name__ == "__main__":
    plant_info = [("Rose", 25, 30), ("Cactus", 3, -5)]
    plants = []
    print("== Garden Security System ===")
    for i in range(1):
        plants = plants + [Plant(*plant_info[i])]
        print("")
        plants[i].set_height(-3)
        # print("")
        # plants[i].set_age(-5)
        print(f"\nCurrent plant: {plants[i].name} ({plants[i]._height},"
              f" {plants[i]._age})")
