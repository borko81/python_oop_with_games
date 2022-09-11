from abc import ABC, abstractmethod


class Fruit:

    def show_name(self):
        raise NotImplementedError('This function not allowed to be implemented')


class AbstractFruit(ABC):
    @abstractmethod
    def show_name(self):
        pass


class Apple(AbstractFruit):
    def show_name(self):
        return "This is apple"


a = Apple()
a.show_name()
