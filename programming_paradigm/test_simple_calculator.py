import unittest
import math
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 3), -3)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero

    def test_edge_cases(self):
        """Test edge cases for all operations."""
        self.assertEqual(self.calc.add(float('inf'), 1), float('inf'))
        self.assertTrue(math.isnan(self.calc.subtract(float('inf'), float('inf'))),
                        "Subtracting infinity from infinity should result in NaN")
        self.assertEqual(self.calc.multiply(-1, float('inf')), -float('inf'))
        self.assertTrue(math.isnan(self.calc.multiply(float('inf'), 0)),
                        "Multiplying infinity by 0 should result in NaN")

if __name__ == "__main__":
    unittest.main()
