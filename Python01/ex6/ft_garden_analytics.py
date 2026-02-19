class Validation:
    """
    shows how static methods work
    you dont initialise this class its
    just used to store utilities
    functions
    """
    @staticmethod
    def check_height(num) -> str:
        if num < 0:
            return 0
        return 1


class GardenManager:
    """
    A manager which manages all the gardens it
    creates, it has a class method which allows
    it to initiate it self.
    Its also got a nested class so that the class
    has a limited scope
    """
    def __init__(self):
        """
        initialises manager adds a garden list
        """
        self.gardens = []

    @classmethod
    def create_garden_network(cls):
        """
        classmethod to create itself
        """
        manager = cls()
        return manager

    class GardenStats():
        """
        nested class which calculates all relevant
        stats
        """
        def __init__(self, manager):
            """
            initialises manager
            """
            self.manager = manager

        def heights(self):
            """
            calculates using the utility function
            weather height is valid
            """
            for garden in self.manager.gardens:
                for plant in garden.plants:
                    if Validation.check_height(plant.height) == 0:
                        print("Height validation test: False")
                        return
            print("Height validation test: True")

        def scores(self):
            """
            calculates the total score depending on the
            plants in the garden
            """
            print("Garden scores - ", end="")
            first = 0
            for garden in self.manager.gardens:
                total = 0
                for plant in garden.plants:
                    total += plant.height
                    if plant.__class__.__name__ == "FloweringPlant":
                        total += 10
                    if plant.__class__.__name__ == "PrizeFlower":
                        total += plant.points
                        total += 20
                if first == 1:
                    print(", ", end="")
                else:
                    first = 1
                print(f"{garden.name}: {total}", end="")
            print("")

        def total_gardens(self):
            """
            calculates how many gardens there are
            in the manager
            """
            total = 0
            for garden in self.manager.gardens:
                total += 1
            print(f"Total gardens managed: {total}")

    def show_garden_stats(self):
        """
        calls all stats functions
        """
        stats = self.GardenStats(self)
        stats.heights()
        stats.scores()
        stats.total_gardens()

    def add_garden(self, name):
        """
        adds a new empty garden by their
        name
        """
        new_garden = Garden(name)
        self.gardens = self.gardens + [new_garden]
        return new_garden


class Garden:
    """
    garden class that sets a generic garden template
    """
    def __init__(self, name):
        """
        initialises garden
        """
        self.name = name
        self.plants = []
        self.total_plants_added = 0
        self.total_growth = 0
        self.plant_types = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}

    def add_plant(self, name, height, colour=None, points=None):
        """
        adds plants to the garden updating relevant fields
        """
        plant = Plant.create(name, height, colour, points)
        self.plant_types[plant.__class__.__name__] += 1
        self.plants = self.plants + [plant]
        self.total_plants_added += 1
        print(f"Added {name} to {self.name}'s garden")

    def grow_all(self):
        """
        grows all the plants in the garden by 1cm
        """
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def garden_info(self):
        """
        lists all stats about the garden
        """
        print(f"==== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.plant_info()
            if plant.__class__.__name__ != "Plant":
                plant.flower_info()
            if plant.__class__.__name__ == "PrizeFlower":
                plant.prize_info()
            print("")
        print(f"\nPlants added: {self.total_plants_added}"
              f", Total growth: {self.total_growth}cm")
        print(f"Plant types: {self.plant_types['Plant']} regular"
              f", {self.plant_types['FloweringPlant']} flowering"
              f", {self.plant_types['PrizeFlower']} prize flowers\n")


class Plant:
    """
    generic template for a plant
    """
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @classmethod
    def create(cls, name, height, colour=None, points=None):
        """
        decides weather it should create a plant, a floweringplant
        or a prizeplant
        """
        if colour is None and points is None:
            return Plant(name, height)
        elif colour is not None and points is None:
            return FloweringPlant(name, height, colour)
        return PrizeFlower(name, height, colour, points)

    def grow(self):
        """
        grows plant by 1
        """
        self.height += 1
        print(f"{self.name} grew 1cm")

    def plant_info(self):
        """
        gives basic info on plant
        """
        print(f" - {self.name}: {self.height}cm", end="")


class FloweringPlant(Plant):
    """
    child of the plant carries over the plant functions
    as well as taking in 1 more arg
    """
    def __init__(self, name, height, colour):
        """
        same as plant but also takes in colour
        """
        super().__init__(name, height)
        self.colour = colour

    def flower_info(self):
        """
        displays the extra info that plant doesnt have
        """
        print(f", {self.colour} flowers (blooming)", end="")


class PrizeFlower(FloweringPlant):
    """
    child of the FloweringPlant carries over everything
    from plant and floweringplant as well as 1 more
    arg
    """
    def __init__(self, name, height, colour, points):
        """
        initialises prizeflower
        """
        super().__init__(name, height, colour)
        self.points = points

    def prize_info(self):
        """
        adds the last extra info relevant to prize
        plats
        """
        print(f", Prize points: {self.points}", end="")


def demo():
    """
    my tests
    """
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager.create_garden_network()
    alices = manager.add_garden("Alice")
    alices.add_plant("Oak Tree", 100)
    alices.add_plant("Rose", 25, "red")
    alices.add_plant("Sunflower", 50, "yellow", 10)
    print("")
    alices.grow_all()
    print("")
    bob_plant = Plant.create("Rose", 25)
    bob_flower = Plant.create("Tulip", 5, "blue")
    bob_prize = Plant.create("Cactus", 27, "green", 5)
    bobs = manager.add_garden("Bob")
    bobs.plants = bobs.plants + [bob_plant] + [bob_flower] + [bob_prize]
    alices.garden_info()
    manager.show_garden_stats()


demo()
