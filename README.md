# EVOLUTIONARY COMPUTING PROJECT (PYTHON)
When given a series of x and y coordinates, this program finds an equitation that maps to those points.

## Example Gif
![ECSystem Demo Python](ECSystemPython.gif)

## About This Project
### Origin
This project was initially written in Java for a class project (details on that project can be seen here <link>).  This exercise was about seeing what it would be like to rewrite a program in a different language.

### Functionality
To run this Evolutionary Computing System, you need to first set up a few parameters first.

  * Generation size => How many Individuals do we want in each generation?
  * Genome size => We can cap the length for how long we want our initial population's expressions to be
  * X-Training Data => The x value we will plug into our random expressions
  * Y-Training Data => The y values we will match our output to to determine fitness
  * Fitness Threshold => What percentage of the population will be selected to go on to the next generation
  *  Stagnation Threshold => If our fitness is not improving overall over this set number of generations, we reboot the system and start over
  *  Mutation Percentage => Of the Individuals selected for the next generation, what percentage will we mutate instead of crossover
  *  Success Threshold => Determines when we have found an equivalent expression. Their fitness is at or below this value.
  
Once all parameters are set, you may pass them to the ECSystem and you are ready to go.

![ECSystemParameters Python](ECSystemParametersPython.png)

## Outside Code
To evaluate the string expressions in the Evolutionary Computing System I used py-expression-eval by Axiacore.

https://github.com/Axiacore/py-expression-eval
