from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def harakatlan(self):
        pass


class Mashina(Transport):
    def harakatlan(self):
        print("Mashina yo'lda harakatlanmoqda.")


class Velosiped(Transport):
    def harakatlan(self):
        print("Velosiped yo'lda harakatlanmoqda.")


Mashina().harakatlan()
Velosiped().harakatlan()