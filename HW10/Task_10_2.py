# 1.
# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
# ball1 = new Ball();
# ball2 = new Ball("super");

# ball1.ball_type     //=> "regular"
# ball2.ball_type     //=> "super"
class Ball:
    def __init__(self, btype="regular"):
        self.ball_type = btype


ball1 = Ball()
print(ball1.ball_type)
ball2 = Ball("super")
print(ball2.ball_type)

# 2.
# Color Ghost
# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
# ghost = new Ghost();
# ghost.color //=> "white" or "yellow" or "purple" or "red"

import random


class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


ghost = Ghost()
print(ghost.color)
ghost2 = Ghost()
print(ghost2.color)


# 3.
# According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
# You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve). The first object in
# the array should be an instance of the class Man. The second should be an instance of the class Woman. Both objects have to be subclasses of Human.
# Your job is to implement the Human, Man and Woman classes.


class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} is men")


class Woman(Human):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} is women")


def God():
    return [Man("Adam"), Woman("Eve")]


# 4.
# Your task is to complete this Class, the Person class has been created. You must fill in the Constructor method
# to accept a name as string and an age as number, complete the get Info property and getInfo method/Info getter which should return johns age is 34

class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"


# 5.
# Now that we have a Block let's move on to something slightly more complex: a Sphere.

import math


class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = None

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        self.volume = round(((4 / 3) * math.pi * self.radius ** 3), 5)
        return self.volume

    def get_surface_area(self):
        return round((4 * math.pi * self.radius ** 2), 5)

    def get_density(self):
        return round(self.mass / self.volume, 5)


# 6.
# Although Timmy had no idea why changing name is so important for his boss, he realized, that it's not the end,
# so he turned to you, his guru, to help him and asked you to prepare some function, which could change name of given class.
# Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers),
# but starting only with upper case letter. In other case it should raise an exception.

def class_name_changer(cls, new_name):
    setattr(cls, "__name__", new_name)
    return cls
