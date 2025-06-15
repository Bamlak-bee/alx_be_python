import unittest
from simple_calculator import SimpleCalculator


class TextClass (unittest.TestCase):
    """Test class for SimpleCalculator."""
    
    def setUp(self):
        # Set up a SimpleCalculator instance before each test
        self.calculator = SimpleCalculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(3, 5), -2)
        self.assertEqual(self.calculator.subtract(-3, -5), -2)
        self.assertEqual(self.calculator.subtract(3, -5), 8)
        self.assertEqual(self.calculator.subtract(-3, 5), -8)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 5), -5)
        self.assertEqual(self.calculator.multiply(-1, 0), 0)
        self.assertEqual(self.calculator.multiply(1, 0), 0)
        self.assertEqual(self.calculator.multiply(1, -8), )

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertIsNone(self.calculator.divide(5, 0))