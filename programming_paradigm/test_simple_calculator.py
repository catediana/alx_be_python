import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.my_calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.my_calc.add(2, 3), 5)
        self.assertEqual(self.my_calc.add(-1, 1), 0)
        self.assertEqual(self.my_calc.add(0, 0), 0)
        self.assertEqual(self.my_calc.add(-3, -7), -10)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.my_calc.subtract(5, 3), 2)
        self.assertEqual(self.my_calc.subtract(0, 5), -5)
        self.assertEqual(self.my_calc.subtract(-2, -3), 1)
        self.assertEqual(self.my_calc.subtract(7, 0), 7)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.my_calc.multiply(2, 3), 6)
        self.assertEqual(self.my_calc.multiply(-2, 3), -6)
        self.assertEqual(self.my_calc.multiply(0, 5), 0)
        self.assertEqual(self.my_calc.multiply(-3, -3), 9)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.my_calc.divide(6, 3), 2)
        self.assertEqual(self.my_calc.divide(-6, 3), -2)
        self.assertEqual(self.my_calc.divide(0, 5), 0)
        self.assertEqual(self.my_calc.divide(-9, -3), 3)

        # Test division by zero
        self.assertIsNone(self.my_calc.divide(5, 0))

   
if __name__ == "__main__":
    unittest.main()
