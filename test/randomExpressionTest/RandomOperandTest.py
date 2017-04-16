import unittest

from src.randomExpression.RandomOperand import RandomOperand


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.operand = RandomOperand(9)

    def test_valid_generation(self):
        self.assertTrue(self.operand.valid_operand(self.operand.generate_operand()))

    def test_invalid_operand_below_range(self):
        self.assertFalse(self.operand.valid_operand("-5"))

    def test_invalid_operand_above_range(self):
        self.assertFalse(self.operand.valid_operand("15"))

    def test_valid_operand_in_range(self):
        self.assertTrue(self.operand.valid_operand("5"))

    def test_valid_operand_x(self):
        self.assertTrue(self.operand.valid_operand("x"))

    def test_invalid_operand_y(self):
        self.assertFalse(self.operand.valid_operand("y"))

if __name__ == '__main__':
    unittest.main()