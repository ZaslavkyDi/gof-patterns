from abc import ABC, abstractmethod

from gof.generating.abstract_factory.product_car import Car, SportCar, Truck
from gof.generating.abstract_factory.product_raly import Rally, SportRally, TruckRally


class RallyFactory(ABC):

    @abstractmethod
    def create_rally(self, car: Car) -> Rally:
        pass

    @abstractmethod
    def create_car(self) -> Car:
        pass


class SportRallyFactory(RallyFactory):

    def create_rally(self, car: SportCar) -> Rally:
        return SportRally(car)

    def create_car(self) -> SportCar:
        return SportCar("1400 h/p")


class TruckkRallyFactory(RallyFactory):

    def create_rally(self, car: Truck) -> Rally:
        return TruckRally(car)

    def create_car(self) -> Truck:
        return Truck("20 t")

