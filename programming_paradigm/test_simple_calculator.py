import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up the calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test addition method."""
        self.assertEqual(self.calc.add(5, 5), 10)
        self.assertEqual(self.calc.add(10, 0), 10)
        self.assertEqual(self.calc.add(8, -2), 6)

    def test_subtract(self):
        """Test subtraction method."""
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(8, -2), 10)

    def test_multiply(self):
        """Test multiplication method."""
        self.assertEqual(self.calc.multiply(5, 5), 25)
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(8, -2), -16)

    def test_divide(self):
        """Test division method."""
        self.assertEqual(self.calc.divide(5, 5), 1)
        self.assertEqual(self.calc.divide(8, -2), -4)
        # Handling division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
    
    def test_divide_by_zero(self):
        """Test division by zero error handling."""
        result = self.calc.divide(10, 0)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
