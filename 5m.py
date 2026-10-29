from abc import ABC, abstractmethod


class Tolov(ABC):
    @abstractmethod
    def tolash(self, summa):
        pass


class NaqdTolov(Tolov):
    def tolash(self, summa):
        print(summa, "so'm naqd pul orqali to'landi.")


class KartaTolovi(Tolov):
    def tolash(self, summa):
        print(summa, "so'm karta orqali to'landi.")


NaqdTolov().tolash(50000)
KartaTolovi().tolash(50000)