"""
Question 1:

Write a function that prompts the user for an amount in USD (float), converts it to the equivalent amount in Euro (EUR), and prints the result.

Currency Conversion Rates:

1 USD = 0.94 EUR

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. the code that calls the function.
"""

# Pseudocode:
# Prompt the user for an amount in USD
# Take the input, convert it to a float
# Convert it to EUR value
# Print the converted float

def convertusdeur():
    amount = float(input('Please enter an amount in USD:'))
    convert = amount * 0.94
    print(f'This is the amount of Euro, the USD amount you entered is worth: {convert:.02f}')

convertusdeur()