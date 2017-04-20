# EVOLUTIONARY COMPUTING PROJECT (PYTHON)
This program is able to generate an expression which equates to a given set of x and y coordinates.

For example, when given the coordinates (-31, 640), (-11,80), (1,0) and (20, 266), it will produce an expression like:  
  
    (x/x/3)+(x+6/x\*x-x+x\*x-7-x\*x/3)
  
## Sample Output
![ECSystem Demo Python](ECSystemPython.gif)

## Sample Code
```python
    def _create_new_generation(self):
        """
        Creates a new generation from the most fit Individuals who were both mutated
        and crossed
        """

        # make sure we only dealing with the most fit Individuals
        most_fit_individuals = self._perform_selection()

        self.stats.add_generation()

        # makes sure we have at least 2 Individuals to work with, there are occasions when most
        # expressions have divide by zero errors where we just need to reboot the system
        if len(most_fit_individuals) > 1 and self._fitness_improving(most_fit_individuals[0]):

            # remove and mutate selected Individuals from the List
            mutated_individuals = self._mutation_selection(most_fit_individuals)

            # each generation is kept at the same size, this determines how many children
            # are need to make this next generation equal the generation size parameter
            num_of_children_needed = self.parameters.generation_size \
                                     - len(most_fit_individuals) - len(mutated_individuals)

            # cross the non mutated Individuals as many times as needed
            children = self._crossover_selection(most_fit_individuals,
                                                 num_of_children_needed,
                                                 self.stats.number_of_gen)

            # combine all three lists to create new generation
             self.generation = mutated_individuals + most_fit_individuals + children
        else:

            # reboot system but continue to keep track of generation count
            self.generation = self._create_initial_population(self.stats.number_of_gen)
            self.stagnation_count = 0
            self.stats.add_system_rebooted()
```

## About This Project
### Origin
This is a python version of a [java program](https://github.com/rossweinstein/Evolutionary-Computing-Java) I wrote in the summer of 2016.  I am newer to python and became interested in what it would be like to rewrite a program in a different langugae.  I found this project helpful in many ways because I not only saw how much I've progressed as a developer since I wrote the original, but it also gave me a better understanding of python and java as I worked through the bugs and design decisions.

### Installation
This project is not available through pip.  To use the code you must clone this repository.
```
$ git clone https://github.com/rossweinstein/Evolutionary-Computing-Python
```

### How To Use
To run this program, you simply pass a set of ECSystemParameters to the ECSystem class.

```python
params = ECSystemParameters()

# Governs the number of expressions in each generation
params.generation_size = 200

# Governs the length of the expressions in the initial population
params.genome_size = 15

# The percentage of the population selected for the next generation
params.fitness_threshold = 0.2

# If our fitness is not improving over this set number of generations, the EC System reboots
params.stagnation_threshold = 30

# The percentage of the population selected for mutation
params.mutation_percentage = .1

# Minimum fitness value required for the system to deem the expression equivalent to training data
params.success_threshold = 0.01

# Trainging Data: The x and y values used to evaluate the expression's fitness
params.x_training_data = [-55.0, -35.0, -11.0, -1.0, 1.0, 19.0, 87.0, 101.0]
params.y_training_data = [1512.0, 612.0, 60, 0.0, 0.0, 180.0, 3784, 5100.0]

ec_system = ECSystem(params)
ec_system.run_ec_system()

# System results
print(ec_system.stats)
```
### Testing
I used PyUnit for all the testing in the project. Those tests can be seen in the [test](https://github.com/rossweinstein/Evolutionary-Computing-Python/tree/master/test) folder.

## Outside Code
I used [py-expression-eval](https://github.com/Axiacore/py-expression-eval) by [Axiacore](https://axiacore.com) to evaluate the string expressions in my program.

## License
[MIT License](https://en.wikipedia.org/wiki/MIT_License)


