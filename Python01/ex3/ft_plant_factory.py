class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self .age = age


plants_info = [("Rose", 25, 30), ("Oak", 200, 365), ("Cactus", 5, 90),
              ("Sunflower", 80, 45), ("Fern", 15, 120)]
plants = []
for i in range(5):
    plants = plants + [Plant(*plants_info[i])]
    print(f"Created: {plants[i].name} ({plants[i].height}cm,"
          f" {plants[i].age} days)")

print(f"\nTotal plants created: {i + 1}")
