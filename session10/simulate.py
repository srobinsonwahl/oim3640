"""
simulate 10 times
each simulate
    roll 100 dice
    display sum of 100 rolls
"""

"""
Function 1: one simulation, rolling 100 dice - generating 100 random integers between 1 and 6 and sum up
Pseudocode:
- create a variable to store the sum, initialize it to 0
- repeat the following step(s) 100 times:
    - generate a random number between 1 and 6
    - add the random number to the sum variable
- print the sum


Function 2: repeat the simulation 10 times
Pseudocode:
- repeat the following step 10 times
    - call function 1
"""

import random

def one_simulation(n=100, sides=6):
    """
    one simulation, rolling n dice, returns the sum
    """
    total = 0

    for i in range(n):
        random_number = random.randint(1, sides)
        total += random_number
    return(total)
    
def repeat_simulations(n=10):
    """
    repeat simulation 10 times
    """
    for i in range(n):
        result = one_simulation(n = 1000, sides = 20)
        print(f'Simulation {i + 1}: sum = {result}')

# repeat_simulations()

# Write a function to simulate rolling 100 dice and count how many simulations it takes to reach toa sum of 600.



def while_roll():
    roll = 0 
    total = 0

    while total <= 400:
        total = one_simulation()
        roll += 1
    
    print(f'Roll: {roll} | Sum: {total}')
    
while_roll()

