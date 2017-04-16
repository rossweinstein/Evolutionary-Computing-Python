import unittest

from src.ecSystem.CalculateDelta import CalculateDelta


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calc = CalculateDelta()
        self.expression1 = "x * 2"
        self.expression2 = "x * x / x"
        self.x_data = [0,1,2,3,4,5]
        self.y_data = [0,2,4,6,8,10]

    def test_find_delta(self):
        self.calc.calculate_delta(self.expression1, self.x_data, self.y_data)
        assert self.calc.delta == 0.0


    def test_divide_by_zero(self):
        self.calc.calculate_delta(self.expression2, self.x_data, self.y_data)
        assert self.calc.y_values == []

if __name__ == '__main__':
    unittest.main()
