class Plant:
    """
    general class of a plant
    """
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    child class of the class Plant
    carries over the name, height and age
    structure but adds the bloom method
    and colour
    """
    def __init__(self, name, height, age, colour):
        super().__init__(name, height, age)
        self.colour = colour

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    child class of the class Plant
    carries over the name, height and age
    structure but adds the produce_shade method
    and trunk_diameter
    """
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = int((78 / 50) * self.trunk_diameter)
        print(f"{self.name} provides {shade}"
              "square meters of shade")


class Vegetable(Plant):
    """
    child class of the class Plant
    carries over the name, height and age
    structure but adds the nutritional_value method
    and harvest_season
    """
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def nutritional_value(self):
        print(f"{self.name} is rich in vitamin c")


print("=== Garden Plant Types ===")
rose = Flower("Rose", 25, 30, "red")
tulip = Flower("Tulip", 30, 40, "Blue")
oak = Tree("Oak", 500, 1825, 50)
maple = Tree("Maple", 300, 1600, 30)
tomato = Vegetable("Tomato", 80, 90, "summer harvest")
potato = Vegetable("Potato", 50, 45, "autumn harvest")

plants = [rose, tulip, oak, maple, tomato, potato]
for i in range(6):
    print(f"\n{plants[i].name} ({plants[i].__class__.__name__})"
          f": {plants[i].height}cm, {plants[i].age} days, ", end="")
    if plants[i].__class__.__name__ == "Flower":
        print(f"{plants[i].colour} colour")
        plants[i].bloom()
    elif plants[i].__class__.__name__ == "Tree":
        print(f"{plants[i].trunk_diameter}cm diameter")
        plants[i].produce_shade()
    else:
        print(f"{plants[i].harvest_season}")
        plants[i].nutritional_value()
