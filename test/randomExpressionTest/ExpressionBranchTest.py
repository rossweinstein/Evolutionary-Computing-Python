import unittest

from src.randomExpression.ExpressionBranch import ExpressionBranch

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.exp = ExpressionBranch(15)

    def test_created_expression_branch(self):
        assert self.exp.is_valid_branch(self.exp.get_branch()) == True

if __name__ == '__main__':
    unittest.main()
