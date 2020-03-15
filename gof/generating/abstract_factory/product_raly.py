from abc import ABC, abstractmethod

from gof.generating.abstract_factory.product_car import SportCar, Truck


class Rally(ABC):

    def __init__(self, car):
        self.car = car

    @abstractmethod
    def start_rally(self):
        pass


class SportRally(Rally):

    def __init__(self, car: SportCar):
        super().__init__(car)

    def start_rally(self):
        print("Sport rally in Tokyo")
        print(f"Our favorite {self.car.__repr__()}")


class TruckRally(Rally):

    def __init__(self, car: Truck):
        super().__init__(car)

    def start_rally(self):
        print("Truck rally Africa")
        print(f"Our favorite {self.car.__repr__()}")
