import unittest
from prime_numbers import is_prime

class prime_numbersTestCase(unittest.TestCase):

	#Tests for prime_numbers.py

	def test_is_seven_prime(self):

		self.assertTrue(is_prime(7))

	def test_is_three_prime(self):

		self.assertTrue(is_prime(3))

	def test_is_one_prime(self):

		self.assertFalse(is_prime(1))


if __name__ =='__main__':
	unittest.main()