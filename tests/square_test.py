from nose.tools import *
from shapes.square import *

def test_area():
  s = Square(5)
  assert_equal(s.area(), 25)

def test_perimeter():
  s = Square(5)
  assert_equal(s.perimeter(), 20)