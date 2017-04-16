from py_expression_eval import Parser
import math


class CalculateDelta:

    def __init__(self):
        self.delta = -1.0
        self.y_values = []
        self.evaluate = Parser()

    def __str__(self):
        return "Delta: " + str(self.delta) + "\nY Values: " + str(self.y_values)

    def calculate_delta(self, expression, x_data, y_data):

        if self._eval_x_data(expression, x_data):
            self._eval_y_data(y_data)

    def _eval_x_data(self, expression, x_data):

        self.y_values = []

        for x_value in x_data:
            try:
                self.y_values.append(self.evaluate.parse(expression).evaluate({'x': x_value}))
            except ZeroDivisionError:
                self.y_values = []
                return False

        return True

    def _eval_y_data(self, y_data):

        self.delta = 0.0

        for i in range(len(y_data)):
            self.delta += math.fabs(y_data[i] - self.y_values[i])
