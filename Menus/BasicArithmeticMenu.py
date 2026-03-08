from Methods.BasicArithmeticMethods import BasicArithmeticMethods
from Methods.GeneralMethods import GeneralMethods
BASIC_ARITHMETIC_INPUT_MENU = """
What function would you like to use
|—— 1: Addition
|—— 2: Subtraction
|—— 3: Multiplication
|—— 4: Division
|—— 5: Remainder
|—— 99: Back
"""
BASIC_ARITHMETIC_FUNCTIONS = {
"1": BasicArithmeticMethods.addition,
"2": BasicArithmeticMethods.subtract,
"3": BasicArithmeticMethods.multiply,
"4": BasicArithmeticMethods.divide,
"5": BasicArithmeticMethods.remainder,
}
class BasicArithmeticMenu:
    def basic_arithmetic_menu():
        while True:
            print(BASIC_ARITHMETIC_INPUT_MENU)
            choice = GeneralMethods.get_choice()
            if choice == "99":
                print("Exiting Calculator")
                break
            if choice in BASIC_ARITHMETIC_FUNCTIONS:
                print(BASIC_ARITHMETIC_FUNCTIONS[choice](GeneralMethods.get_numbers()))
            else:
                print("Invalid Input...")