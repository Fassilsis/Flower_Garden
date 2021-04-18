import random


class Flower(object):

    def __init__(self, color: str, height: float,
                 hydration: float):
        self.color = color
        self.height = height
        self.hydration = hydration

    def __str__(self):
        return f"Flower {self.color}, with height of {self.height} cm and hydration {self.hydration}%"

class Weather:
    def __init__(self, type:str):
        self.type = type



class Yellow(Flower):
    def __init__(self, height, hydration):
        super().__init__(self, height, hydration)

    def initial_height(self):
        return 6 < self.height > 9

    def initial_hydration(self):
        return 20 < self.hydration > 35

    def effect_on_hydration(self):
        if self.type == 'rainy':
            return self.hydration + 20
        elif self.type == 'cloudy':
            return self.hydration - 5
        elif self.type == 'sunny':
            return self.hydration - 5








def main():
    red = Flower('Red', 3, 30)
    print(red)


main()