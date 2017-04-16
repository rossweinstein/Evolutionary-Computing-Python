import unittest

from src.genome.Individual import Individual
from src.randomExpression.RandomStringExpression import RandomStringExpression


class MyTestCase(unittest.TestCase):

    def setUp(self):

        self.rand_expression = RandomStringExpression(20)
        self.rand_expression2 = RandomStringExpression(20)
        self.genome1 = Individual(self.rand_expression)
        self.genome2 = Individual(self.rand_expression2)

    def test_valid_mutate(self):
        original = self.genome1.genome.get_random_expression()
        self.genome1.mutate(1)
        mutated = self.genome1.genome.get_random_expression()
        self.assertNotEqual(original, mutated)

    def test_valid_crossover(self):
        crossed_genome = self.genome1.crossover(self.genome2, 1)
        self.assertTrue(crossed_genome.genome.is_valid_expression)

if __name__ == '__main__':
    unittest.main()
