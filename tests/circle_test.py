from nose.tools import *
from math import pi
from shapes.circle import *

def test_circumference():
  c = Circle(5)
  assert_equal(c.circumference(),2*5*pi)

def test_diameter():
  c = Circle(5)
  assert_equal(c.diameter(),10)

def test_area():
  c = Circle(5)
  assert_equal(c.area(), pi * 5 ** 2)