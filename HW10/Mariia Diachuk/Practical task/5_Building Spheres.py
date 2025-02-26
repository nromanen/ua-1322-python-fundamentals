class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

sphere = Sphere(2, 10)
print(sphere.get_radius())  # Output: 2
print(sphere.get_mass())    # Output: 10
