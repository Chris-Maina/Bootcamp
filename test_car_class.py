import unittest
from carClass import Car
class CarClassTestCase(unittest.TestCase):
	def test_car_instance(self):
		honda = Car('Honda')
		self.assertIsInstance(honda, Car, msg='The object should be an instance of the `Car` class')