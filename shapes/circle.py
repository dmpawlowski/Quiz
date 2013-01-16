from math import pi

class Circle(object):

  def __init__(self, radius):
    self.radius = radius

  def circumference(self):
    return pi * self.diameter()

  def diameter(self):
    return 2 * self.radius

  def area(self):
    return pi * self.radius ** 2