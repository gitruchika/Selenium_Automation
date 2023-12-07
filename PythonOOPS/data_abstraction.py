"""
Abstraction means to hide the internal implimentation of the application, we have provide overview of the
features instead of actual logic implimentation.

"""

from abc import abstractmethod


class Animal:

    @abstractmethod
    def voice(self):
        """This method provide the animal voice details"""
        pass

    @abstractmethod
    def food(self):
        """This method provide animal details"""
        pass


class Dog(Animal):
    def __init__(self, dog_voice, dog_food):
        self.dog_voice = dog_voice
        self.dog_food = dog_food

    def voice(self):
        print("The voice of dog :", self.dog_voice)

    def food(self):
        print("The food of dog :", self.dog_food)


if __name__ == '__main__':
    obj = Dog('Bark', 'Pedigree')

    obj.voice()
    obj.food()
