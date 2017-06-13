import unittest
from fizz_buzz import fizz_buzz
class FizzBuzzClassTest(unittest.TestCase):

	#test for number correct output
	def test_fizz_1(self):
		self.assertEqual(fizz_buzz(3),'Fizz',msg='should return `Fizz` for number divisible by 3')
		self.assertEqual(fizz_buzz(33),'Fizz',msg='should return `Fizz` for number divisible by 3')
	def test_buzz_1(self):
		self.assertEqual(fizz_buzz(5),'Buzz',msg='should return `Buzz` for number divisible by 5')
		self.assertEqual(fizz_buzz(55),'Buzz',msg='should return `Buzz` for number divisible by 5')
		
