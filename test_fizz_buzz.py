import unittest
from fizz_buzz import fizz_buzz
class FizzBuzzClassTest(unittest.TestCase):

	#test for number divisible by 3
	def test_fizz_1(self):
		self.assertEqual(fizz_buzz(3),'Fizz',msg='should return `Fizz` for number divisible by 3')
		self.assertEqual(fizz_buzz(33),'Fizz',msg='should return `Fizz` for number divisible by 3')
	#test for number divisible by 5
	def test_buzz_1(self):
		self.assertEqual(fizz_buzz(5),'Buzz',msg='should return `Buzz` for number divisible by 5')
		self.assertEqual(fizz_buzz(55),'Buzz',msg='should return `Buzz` for number divisible by 5')
	#test for number divisible by both 3 and 5
	def test_fizz_buzz(self):
		self.assertEqual(fizz_buzz(15),'FizzBuzz',msg='should return `FizzBuzz` for number divisible by 3 and 5')
		self.assertEqual(fizz_buzz(105),'FizzBuzz',msg='should return `FizzBuzz` for number divisible by 3 and 5')
	#test for number indivisible by 3 or 5
	def test_indivisible(self):
		self.assertEqual(fizz_buzz(101),101,msg='should return the number if indivisible by 3 or 5')
		self.assertEqual(fizz_buzz(8),8,msg='should return the number if indivisible by 3 or 5')
  