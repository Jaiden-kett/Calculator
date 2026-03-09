from Methods.NumberTheory import NumberTheoryMethods
from Methods.General import GeneralMethods
MENU = """
What function would you like to use
|—— 1: Greatest Common Divisor
|—— 2: Least Common Multiple
|—— 3: Divisors
|—— 99: Back
"""

operations = {
    "1": NumberTheoryMethods.greatestCommonDivisor,
    "2": NumberTheoryMethods.leastCommonMultiple,
    "3": NumberTheoryMethods.divisors,
}

def number_theory_menu():
    GeneralMethods.menu_functions(MENU, operations)