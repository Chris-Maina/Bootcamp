#Test for prime numners
import unittest
from prime_numbers import printPrimeNumbers

class TestPrimeNumbers(unittest.TestCase):
	"""
	Test if number is prime
	Test for input 0 -> not prime
	Test for input 1
	Test for negatives
	Test for string input
	"""
	def test_correct_output(self):
		self.assertEqual(printPrimeNumbers(10), [2,3,5,7])

	def test_string_inputs(self):
		with self.assertRaises(TypeError)
		
