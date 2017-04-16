from random import randint


class RandomPointsFinder:
    """
    This class finds two indexes within a string and sorts them returning
    the lowest number first
    """

    def __init__(self, expression=None):
        self._expression = expression

    def set_expression(self, expression):
        """
        Setter for this class
        :param expression: The string to find the random points within
        :return:
        """
        self._expression = expression

    def get_points(self):
        """
        Finds the two random points within a string. If the string is only a single
        character long, it returns [0,0]
        :return: List of two ordered integers
        """

        if len(self._expression) == 1:
            return [0, 0]
        else:
            return self._get_even_points()

    def _get_even_points(self):
        """
        It is important for the selection to the be two even numbers. This is because
        the selection will possibly be replaced by a newly created expression which will
        start with an operand. This avoids created any invalid expressions.
        :return: List of two ordered integers
        """

        random_points = self._get_random_points()

        random_points[0] = self._make_even(random_points[0])
        random_points[1] = self._make_even(random_points[1])

        return self._order_points(random_points)

    def _order_points(self, random_points):
        """
        How the program reads the information from this class relies on the first item
        in the last being the smaller number. This ensures that happens.
        :param random_points: The random selection from the string
        :return: List of two ordered integers
        """

        if random_points[0] > random_points[1]:
            temp = random_points[0]
            random_points[0] = random_points[1]
            random_points[1] = temp

        return random_points

    def _get_random_points(self):
        """
        Selects two different random points within a given string.
        :return:  List of two unordered integers
        """

        first_point = randint(0, len(self._expression) - 1)
        second_point = randint(0, len(self._expression) - 1)

        while first_point == second_point:
            second_point = randint(0, len(self._expression) - 1)

        return [first_point, second_point]

    def _make_even(self, number):
        """
        Makes numbers even if odd by subtracting 1.
        :param number: An integer to make even
        :return: int an even integer
        """

        if number % 2 == 0:
            return number
        else:
            return number - 1