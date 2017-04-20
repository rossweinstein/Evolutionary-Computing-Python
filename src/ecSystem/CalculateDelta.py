from py_expression_eval import Parser
import math


class CalculateDelta:
    """
    This class is responsible for all our calculations.  It is able to
    determine an Individual's fitness by finding the difference between
    the supplied training data and the values the expression produces.
    """

    def __init__(self):
        self.delta = -1.0
        self.y_values = []
        self.evaluate = Parser()

    def __str__(self):
        return "Delta: " + str(self.delta) + "\nY Values: " + str(self.y_values)

    def calculate_delta(self, expression, x_data, y_data):
        """
        Evaluates the expression first and sees if it is worth finding the
        Individuals fitness. If there are any divide by zero errors, no
        fitness will be calculated.
        :param expression: The Individual we want to find the fitness for
        :param x_data: training data
        :param y_data: training data
        :return:
        """

        if self._eval_x_data(expression, x_data):
            self._eval_y_data(y_data)

    def _eval_x_data(self, expression, x_data):
        """
        Plugs in all the x training data to see if we have any divide by
        zero errors. If we do, return false because this expression is
        not worth finding the fitness
        :param expression: The Individual we want to find the fitness for
        :param x_data: training data
        :return:
        """

        self.y_values = []

        for x_value in x_data:
            try:
                self.y_values.append(self.evaluate.parse(expression).evaluate({'x': x_value}))
            except ZeroDivisionError:
                self.y_values = []
                return False

        return True

    def _eval_y_data(self, y_data):
        """
        If we have no divide by zero errors, find how this expression differs
        from our training data
        :param y_data: training data
        """

        self.delta = 0.0

        for i in range(len(y_data)):
            self.delta += math.fabs(y_data[i] - self.y_values[i])
