

class Animal:    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years"

## Class inheritance
class Dog(Animal):
    def bark(self):
        print("uf uf" * self.age)

## Class inheritance
class HungarianDog(Dog):
    def bark(self):
        print("vau" * self.age)

## Class inheritance
class RomanianDog(Dog):
    def barking(self):
        print("ham" * self.age)

## Class inheritance
class PolishDog(Dog):
    def bark(self):
        print("cha\l" * self.age)

class SerbianDog(Dog):
    pass


animal_obj = Animal("Boy", 3)
print(animal_obj)
   
dog_obj = RomanianDog("Spike", 10)
print(dog_obj)
dog_obj.bark()
