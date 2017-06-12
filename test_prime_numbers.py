#Test for prime numners
import unittest
from prime_numbers import printPrimeNumbers

class TestPrimeNumbers(unittest.TestCase):
	"""
	Test if number is prime
	Test for float inputs
	Test for null inputs
	Test for negatives
	Test for string input
	"""
	def test_correct_output(self):
		self.assertEqual(printPrimeNumbers(10), [2,3,5,7])

	def test_string_inputs(self):
		#self.assertEqual(printPrimeNumbers('one'), None)
		with self.assertRaises(Exception):
			 printPrimeNumbers('hello')

    def test_negative_inputs(self):
		with 
		self.assertRaises(Exception):
			 printPrimeNumbers(-10)

    def test_null_inputs(self):
		with 
		self.assertRaises(TypeError):
			 printPrimeNumbers()

	def test_float_inputs(self):
		with 
		self.assertRaises(TypeError):
			 printPrimeNumbers(10.2)

 

		
