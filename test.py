import unittest
import calculator   # the file you are testing

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 4), 8)
        self.assertEqual(calculator.multiply(0, 10), 0)

if __name__ == "__main__":
    unittest.main()
