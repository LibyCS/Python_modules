class Plant:
    """
    sets a structure for a class called plant
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        adds variables to each plant by
        initialising straight away
        """
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 12)
    plants = (rose, sunflower, cactus)
    for i in range(0, 3):
        print(f"{plants[i].name}: {plants[i].height}cm,"
              f" {plants[i].age} days old")
