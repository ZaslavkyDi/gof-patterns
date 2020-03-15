from gof.generating.abstract_factory.factory import RallyFactory
from gof.generating.abstract_factory.factory import TruckkRallyFactory
from gof.generating.abstract_factory.factory import SportRallyFactory


class RallyGame:

    def start_rally(self, factory: RallyFactory):
        car = factory.create_car()
        rally = factory.create_rally(car)

        rally.start_rally()

if __name__ == '__main__':
    game = RallyGame()

    rally_factory = TruckkRallyFactory()
    game.start_rally(rally_factory)

    print('\nNEXT RALLY\n')
    rally_factory = SportRallyFactory()
    game.start_rally(rally_factory)