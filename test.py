import unittest

def add(a, b):
    return a + b

class TestSample(unittest.TestCase):

    def test_pass(self):
        # This will PASS
        self.assertEqual(add(2, 3), 5)

    def test_fail(self):
        # This will FAIL
        self.assertEqual(add(2, 2), 5)

if __name__ == "__main__":
    unittest.main()
