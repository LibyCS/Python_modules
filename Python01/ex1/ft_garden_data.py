
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 12)
plants = (rose, sunflower, cactus)
for i in range(0,3):
    print(f"{plants[i].name}: {plants[i].height}cm,"
          f" {plants[i].age} days old")


