from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param: float):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass

class Coat(Clothes):
    @property
    def calculate(self) -> float:
        return round(self.param / 6.5 + 0.5, 2)


class Costume(Clothes):
    @property
    def calculate(self) -> float:
        return round(2 * self.param + 0.3, 2)


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3
