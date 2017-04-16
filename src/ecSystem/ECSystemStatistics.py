import time


class ECSystemStatistics:
    """
    This class keeps track of many items we would like to know from our EC System.
    It will track the most fit Individuals in each generation, the lowest fitness value
    in each generation and their associated y_values, the number of generations,
    the number of times the system needed to reboot, how many operations has the
    program done, how long is it taken, and the expression equivalent.
    """

    def __init__(self):
        self.expression_equivalent = None
        self.most_fit_in_gen = []
        self.most_fit_values = []
        self.most_fit_y_values = {}
        self.number_of_gen = 0
        self.reboot_total = 0
        self.start_time = 0
        self.run_time = 0
        self.operation_count = 0

    def __str__(self):
        return "EC System Stats\n" + "\nNumber Of Generations: " \
               + str(self.number_of_gen) + "\n\nEquivalent Expression:\n" \
               + str(self.expression_equivalent) + "\n\nEC System Run Time: " \
               + "{:.2f} seconds".format(self.run_time) + "\nEC System Reboot Amount: " + str(self.reboot_total) \
               + "\n\nTotal Operations In ECSystem: " + str(self.operation_count)

    def add_generation(self):
        """
        Adds 1 generation to the generation total
        :return:
        """
        self.number_of_gen += 1

    def add_operation(self):
        """
        Adds 1 operation to the operation total
        :return:
        """
        self.operation_count += 1

    def add_system_rebooted(self):
        """
        Adds 1 reboot to the reboot total
        :return:
        """
        self.reboot_total += 1

    def set_successful_genome(self, expression):
        """
        Records the Individual with a fitness level below the provided threshold
        :param expression: Individual with the appropriate fitness level
        :return:
        """
        self.expression_equivalent = expression

    def add_most_fit_in_generation(self, most_fit):
        """
        Updates our most fit trackers
        :param most_fit: Individual who is the most fit in their generation
        :return:
        """
        self.most_fit_in_gen.append(most_fit)
        self.most_fit_values.append(most_fit.fitness)
        self.most_fit_y_values[self.number_of_gen] = most_fit.y_values

    def start_stop_watch(self):
        """
        Starts counting.
        :return:
        """
        self.start_time = time.time()

    def end_stop_watch(self):
        """
        Record how long it took for our system to find an equivalent expression.
        :return:
        """
        end_time = time.time()
        self.run_time = end_time - self.start_time
