from random import randint
from random import getrandbits


class RandomOperand:
    """
    This class handles operands for an expression.  It is able
    to create a random operand and check if a value is deemed a
    valid operand.
    """

    def __init__(self, bound):
        """
        :param bound: The upper limit for the operand
        """
        self._operand = ""
        self._upper_limit = bound

    def __str__(self):
        """
        :return: String representation of the most recent created operand
        """
        return "Operand: " + self._operand

    def generate_operand(self):
        """
        Creates a new operand that is either the variable 'x' or
        a value within the range of 0 to the supplied bound.
        :return: String A newly created operand
        """
        number_not_x = randint(0,10)

        if number_not_x > 4:
            return str(randint(0, self._upper_limit))
        else:
            return "x"

    def valid_operand(self, the_operand):
        """
        Checks whether a String is a valid operand or not
        :param the_operand: The String to validate
        :return: Boolean if the supplied String is a operand or not
        """
        if the_operand == "x":
            return True
        else:
            try:
                return 0 <= int(the_operand) <= self._upper_limit
            except ValueError:
                return False

if __name__ == '__main__':
    operand = RandomOperand(9)
    print(operand.generate_operand())
    print(operand.valid_operand("-5"))
    print(operand.valid_operand("5"))
    print(operand.valid_operand("15"))
    print(operand.valid_operand("x"))
    print(operand.valid_operand("y"))