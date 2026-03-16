class Plant:
    """
    sets a general structure of a plant
    with methods
    """
    def __init__(self, name: str, height: int, ages: int) -> None:
        """
        initialises plants which adds specified
        data to store in variables
        """
        self.name = name
        self.height = height
        self.ages = ages
        self.growth = 0

    def grow(self) -> None:
        """
        a grow method that acts on the class
        """
        if self.name == "Sunflower":
            self.height += 3
            self.growth += 3
        else:
            self.height += 1
            self.growth += 1

    def age(self) -> None:
        """
        method that ages the plant when called
        """
        self.ages += 1
        self.grow()

    def get_info(self) -> None:
        """
        gives info on the plant
        """
        print(f"{self.name}: {self.height}cm, {self.ages} days old")
        if self.growth != 0:
            print(f"Growth this week: *{self.growth}cm")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    for i in range(6):
        rose.age()
    print("=== Day 7 ===")
    rose.get_info()
