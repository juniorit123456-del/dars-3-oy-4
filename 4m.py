from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def harakatlan(self):
        pass


class Mashina(Transport):
    def harakatlan(self):
        print("Mashina harakatlanmoqda.")


class Velosiped(Transport):
    def harakatlan(self):
        print("Velosiped harakatlanmoqda.")


Mashina().harakatlan()
Velosiped().harakatlan()