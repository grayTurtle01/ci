import unittest
from funciones import is_prime

class Tests(unittest.TestCase):
  def test_1(self):
    self.assertFalse(is_prime(1))

  def test_5(self):
    """ Check that 5 is prime """
    self.assertTrue(is_prime(5))

  def test_8(self):
    """ Check that 8 isn't prime """
    self.assertFalse(is_prime(8))

  def test_13(self):
    """ Check that 13 is prime """
    self.assertTrue(is_prime(13))

  def test_25(self):
    """ Check that 25 isn't prime """
    self.assertFalse(is_prime(25))

if __name__ == '__main__':
  unittest.main()
