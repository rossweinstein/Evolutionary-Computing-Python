import unittest

from src.randomExpression.RandomOperator import RandomOperator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.operator = RandomOperator()

    def test_valid_plus(self):
        self.assertTrue(self.operator.valid_operator("+"))

    def test_valid_minus(self):
        self.assertTrue(self.operator.valid_operator("-"))

    def test_valid_divide(self):
        self.assertTrue(self.operator.valid_operator("/"))

    def test_valid_multiply(self):
        self.assertTrue(self.operator.valid_operator("*"))

    def test_invalid_operand(self):
        self.assertFalse(self.operator.valid_operator("432"))

    def test_invalid_type_operator(self):
        self.assertFalse(self.operator.valid_operator(8))

if __name__ == '__main__':
    unittest.main()
