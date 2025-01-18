class Person:
    def __init__(self, name, age):
        # private attributes
        self.__name = name
        self.__age = age

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        self.__name = name

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")


# Creating an object of the class
person = Person("Alice", 30)

# Accessing data through getter methods
print(f"Name: {person.get_name()}, Age: {person.get_age()}")

# Using setter method to change name and age
person.set_name("Bob")
person.set_age(35)
print(f"Updated Name: {person.get_name()}, Updated Age: {person.get_age()}")
from abc import ABC, abstractmethod

# Abstract Class (Abstraction)
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method, to be implemented by subclasses

    @abstractmethod
    def move(self):
        pass  # Another abstract method to be implemented

# Concrete Class 1
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def move(self):
        return "The dog runs"

# Concrete Class 2
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

    def move(self):
        return "The cat walks gracefully"

# Concrete Class 3
class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

    def move(self):
        return "The bird flies"

# Main Program
def demonstrate_abstraction():
    # Creating objects of concrete classes
    dog = Dog()
    cat = Cat()
    bird = Bird()

    # Calling the abstract methods implemented in the subclasses
    print(f"Dog: {dog.make_sound()} and {dog.move()}")
    print(f"Cat: {cat.make_sound()} and {cat.move()}")
    print(f"Bird: {bird.make_sound()} and {bird.move()}")

# Demonstrating Abstraction
demonstrate_abstraction()