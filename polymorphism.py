from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class Human(animal):
    def move(self):
        print("I can walk and run")
class Dog(animal):
    def move(self):
        print("I can bark")
class Snake(animal):
    def move(self):
        print("I can crawl")
R=Human()
R.move()
d=Dog()
d.move()
y=Snake()
y.move()