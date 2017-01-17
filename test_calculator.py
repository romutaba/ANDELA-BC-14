import unittest

from calculator import calculate


class TestOperation(unittest.TestCase):

	def test_sum(self):
		self.assertEqual(calculate(2, 3, 'sum'), 5)

	def test_subtract(self):
		self.assertEqual(calculate(5, 10, 'subtract'), -5)

	def test_multiply(self):
		self.assertEqual(calculate(5, 10, 'multiply'), 50)

	def test_divide(self):
		self.assertEqual(calculate(5, 10, 'divide'), 0.5)

	def test_quadratic(self):
		self.assertEqual(calculate(3,2, 'quadratic'), 9)
		

if __name__ == '__main__':
	unittest.main()
		