from math import pi, pow

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = float(radius)
        self.mass = float(mass)
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round((4 / 3) * pi * pow(self.radius, 3), 5)
    
    def get_surface_area(self):
        return round(4 * pi * pow(self.radius, 2), 5)
                    
    def get_density(self):
        return round((self.mass / self.get_volume()), 5)