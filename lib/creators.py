#by Dev2
from abc import ABC, abstractmethod
from lib.products import *


class Manager(ABC):

    def __init__(self, point: str, destination: str, term: float, client :str):
        self._point = point
        self._destination = destination
        self._client = client


    # @abstractmethod
    # def delivery_order(self):
    #     pass

    def delivery_order(self):
        print(f'Принят заказ от {self._client} на перевозку из {self._point} в {self._destination}: срок')
        print(f' Транспортная единица - {self.create_transport()}')

    @abstractmethod
    def create_transport(self):
        pass

class RoadManager(Manager):

    def __init__(self, point: str, destination: str, term: float, client: str):
        super().__init__(point, destination, term, client)

    def delivery_order(self):
        print (f'Принят заказ от {self._client} на перевозку из {self._point} в {self._destination}: срок')
        #pass
        print(f' Транспортная единица - {self.create_transport()}')


    def create_transport(self):
        return Truck('Трейлер', 'GM', 25, 4.5)


        #pass


class RiverManager(Manager):

    def __init__(self, point: str, destination: str, term: float, client: str):
        super().__init__(point, destination, term, client)

    # def delivery_order(self):
    #     print (f'Принят заказ от {self._client} на перевозку из {self._point} в {self._destination}: срок')
    #     #pass
    #
    #     print(f' Транспортная единица - {self.create_transport()}')


    def create_transport(self):
        return Ship('Сухогруз', 'Днепр', 50000, 6.5)


class AirManager(Manager):

    def __init__(self, point: str, destination: str, term: float, client: str):
        super().__init__(point, destination, term, client)

    # def delivery_order(self):
    #     print (f'Принят заказ от {self._client} на перевозку из {self._point} в {self._destination}: срок')
    #     #pass
    #
    #     print(f' Транспортная единица - {self.create_transport()}')


    def create_transport(self):
        return AirPlane('Транспортник', 'АН-35', 5, 4.5)
