class Plant:
    def __init__(self, name, height, ages):
        self.name = name
        self.height = height
        self.ages = ages
        self.growth = 0
    def grow(self):
        if self.name == "Sunflower":
            self.height += 3
            self.growth += 3
        else:
            self.height += 1
            self.growth += 1
    def age(self):
        self.ages += 1
        self.grow()
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.ages} days old")
        if self.growth != 0:
            print(f"Growth this week: *{self.growth}cm")

rose = Plant("Rose", 25, 30)
print("=== Day 1 ===")
rose.get_info()
for i in range(6):
    rose.age()
print("=== Day 7 ===")
rose.get_info()
