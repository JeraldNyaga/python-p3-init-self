#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt",favourite_toy="Any"):
        self.name = name
        self.favourite_toy = favourite_toy
        self.breed = breed

    def bark(self):
        print("Woof!")

    def get_adopted(self, ownner_name):
        self.owner = ownner_name

    def showing_self(self):
        return self

fido = Dog("Fido")
snoopy = Dog("Snoopy")

print(fido.name)
print(snoopy.name)

fido.get_adopted("Mark")
snoopy.get_adopted("Susan")
print(fido.owner)
print(snoopy.owner)