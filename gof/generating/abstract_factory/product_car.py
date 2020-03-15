class Car:

    def __repr__(self):
        print(f"Class -> {self.__class__}")


class SportCar(Car):

    def __init__(self, engine):
        self.engine = engine

    def __repr__(self):
        print(f"Sport car -> "
              f"    engine: {self.engine};")


class Truck(Car):

    def __init__(self,max_power):
        self.max_power = max_power

    def __repr__(self):
        print(f"Tuck car -> "
              f"    max_power: {self.max_power}")
