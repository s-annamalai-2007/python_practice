#=========CLASS AND OBJECT
# Define a simple Car class
class Car:
    # The constructor method initializes the attributes
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # A regular method to display information
    def display_info(self):
        print(f"This is a {self.brand} {self.model}.")

# Create an object (instance) of the Car class
my_car = Car("Toyota", "Corolla")

# Call the object's method
my_car.display_info()
# Output: This is a Toyota Corolla.

'''
#=================== INHERITENCE
# Parent class
class Animal:
    def eat(self):
        print("This animal is eating.")

# Child class inherits from Animal
class Dog(Animal):
    def bark(self):
        print("The dog is barking.")

# Create an object of the child class
my_dog = Dog()

# Access inherited method and own method
my_dog.eat()   # Output: This animal is eating.
my_dog.bark()  # Output: The dog is barking.


# ===================POLYMORPHISM
class Cat:
    def make_sound(self):
        print("Meow")

class Cow:
    def make_sound(self):
        print("Moo")

# A function that takes any object and calls its make_sound method
def play_sound(animal_object):
    animal_object.make_sound()

# Create objects
my_cat = Cat()
my_cow = Cow()

# Same function produces different behaviors depending on the input object
play_sound(my_cat)  # Output: Meow
play_sound(my_cow)  # Output: Moo


#===============ENCAPSULATION 
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    # Public method to securely check the balance
    def check_balance(self):
        print(f"Account balance: ${self.__balance}")

    # Public method to modify private data safely
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")

# Create an account
account = BankAccount("Alice", 1000)

# account.__balance  # This would raise an AttributeError
account.check_balance()  # Output: Account balance: $1000
account.deposit(500)     # Output: Deposited $500
account.check_balance()  # Output: Account balance: $1500


#==================== ABSTRACTION 
from abc import ABC, abstractmethod

# Abstract base class (cannot be instantiated directly)
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Motorcycle(Vehicle):
    # The child class MUST implement the abstract method
    def start_engine(self):
        print("Motorcycle engine started. Vroom!")

# Create an object of the concrete subclass
my_bike = Motorcycle()
my_bike.start_engine()  # Output: Motorcycle engine started. Vroom!
'''