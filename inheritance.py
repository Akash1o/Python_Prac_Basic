class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def dis(self):
        print(f"Name: {self.name} Color: {self.color}")

# child class inherits from Car
class Ferrari(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color)
        self.speed = speed

    def dis(self):
        print(f"Name: {self.name} Color: {self.color} Speed: {self.speed}")

# creating object of Ferrari
fer1 = Ferrari("Ferrari", "Red", 200)
fer1.dis()