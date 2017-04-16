import unittest

from src.randomExpression.RandomStringExpression import RandomStringExpression


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.exp = RandomStringExpression(size=15)

        child = ["x+5+2-x", "/", "x/4-2"]
        self.rand_str_exp2 = RandomStringExpression(child_expression=child)

    def test_generated_random_string_expression(self):
        self.assertTrue(self.exp.is_valid_expression())

    def test_supplied_random_string_expression(self):
        self.assertTrue(self.rand_str_exp2.is_valid_expression())

if __name__ == '__main__':
    unittest.main()
