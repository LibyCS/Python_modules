
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        print(f"Plant created: {name}")
        self.height = 0
        self.set_height(height)
        self.age = 0
        self.set_age(age)
    def set_height(self, height):
        if height >= 0:
            self.height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print("Invalid operation attempted:"
                  f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
    def set_age(self, age):
        if age >= 0:
            self.age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print("Invalid operation attempted:"
                  f" age {age} days [REJECTED]")
            print("Security: Negative age rejected")
    def get_height(self):
        print(f"{self.name} height is {self.height}cm")
    def get_age(self):
        printf(f"{self.name} age is {self.age} days")

plant_info = [("Rose", 25, 30), ("Cactus", 3, -5)]
plants = []
print("== Garden Security System ===")
for i in range(2):
    plants = plants + [Plant(*plant_info[i])]
    print("")
    plants[i].set_height(-3)
    print("")
    plants[i].set_age(-5)
    print(f"\nCurrent plant: {plants[i].name} ({plants[i].height},"
          f" {plants[i].age})")
