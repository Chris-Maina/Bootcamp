import unittest
from fizz_buzz import fizz_buzz
class FizzBuzzClassTest(unittest.TestCase):

	#test for number correct output
	def test_fixx_1(self):
		self.assertEqual(fizz_buzz(3),'Fizz',msg='should return `Fizz` for number divisible by 3')
		
