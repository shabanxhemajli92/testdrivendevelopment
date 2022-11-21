import unittest
import functions_totest as f


class TestClass(unittest.TestCase):
    def test_string(self):
        self.assertEqual("Shaban is", f.string())

    def test_integer(self):
        self.assertEqual(2, f.integer())

    def test_addition(self):
        self.assertEqual(9, f.addition(4, 5))


if __name__ == '__main__':
    unittest.main()
