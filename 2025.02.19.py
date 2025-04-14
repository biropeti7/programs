from abc import ABC, abstractmethod

class Shape:
        @abstractmethod
        def area(self):
                pass
        
class Shape(ABC):
        @abstractmethod
        def area(self):
                pass
        
class Circle(Shape):
        def __init__(self, radius) -> None:
                self.radius = radius
        def area(self):
                return 3.14 * self.radius**2

class Square(Shape):
        def __init__(self, side) -> None:
                self.side = side
        def area(self):
                return self.side**2

class Triangle(Shape):
        def __init__(self, base, height) -> None:
                self.base = base
                self.height = height
        def area(self):
                return 0.5* self.base * self.height

class Pizza(Circle):
        def __init__(self, radius, topping):
                super().__init__(radius)
                self.topping = topping

shapes = [Circle(5), Square(4), Triangle(3, 6), Pizza(3, "jalapeno")]

for shape in shapes:
        print(shape.area())




def Hello():
        print("HELLO")
obj = Hello
obj()

def Hello(fn):
        def inner():
                print("hello", end=" ")
                fn()
        return inner

def world():
        print("World! 1")
        
decorated = Hello(world)
decorated()
@Hello
def world():
        print("world 2")
world()
@Hello
def world():
        print("world 3")
world()

import time

def measure_time(fn):
        def inner(*args, **kwargs):
                start = time.time()
                resault = fn(*args, **kwargs)
                end  = time.time()
                print(end - start)
                return resault
        return inner
                
@measure_time
def HI():
        time.sleep(1)
        print("Hello, World!", end= " ")
        
HI()
                
                
                
class Animal:
        alive = True
class Dog(Animal):
        def speak(self):
                print("Woof!")
class Cat(Animal):
        def speak(self):
                print("Meeow!")
                
class Car:
        def horn(self):
                print("Beep!")
                                
        def speak(self):
                self.horn()
                
animals = [Dog(), Cat(), Car()]
for animal in animals:
        animal.speak()
        print(Animal.alive)
