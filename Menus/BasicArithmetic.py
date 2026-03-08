from Methods.BasicArithmetic import BasicArithmeticMethods
from Methods.General import GeneralMethods

MENU = """
What function would you like to use
|—— 1: Addition
|—— 2: Subtraction
|—— 3: Multiplication
|—— 4: Division
|—— 5: Remainder
|—— 99: Back
"""

operations = {
"1": BasicArithmeticMethods.add,
"2": BasicArithmeticMethods.subtract,
"3": BasicArithmeticMethods.multiply,
"4": BasicArithmeticMethods.divide,
"5": BasicArithmeticMethods.remainder,
}

def basic_aritmetic_menu():
    GeneralMethods.menu_functions(MENU, operations)