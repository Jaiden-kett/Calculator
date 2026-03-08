from Menus.BasicArithmeticMenu import BasicArithmeticMenu
from Methods.GeneralMethods import GeneralMethods
import sys
MAIN_MENU = """
What type of Calculator would you like to use?
|—— 1. Basic Arithmetic
|—— 2. Power & Roots
|—— 3. Number Theory
|—— 4. Statistics & Data Analysis (In Progress)
|—— 5. Trigonometry & Logarithms (Coming soon)
|—— 6. Bitwise / Programmer Functions (Coming soon)
|—— 7. Memory Functions (Coming soon)
|—— 8. Number Utilities (Coming soon)
|—— 9. Unit Conversions (Coming soon)
|—— 10. Advanced Features (Coming soon)
|—— 99. Exit
"""
BASIC_MENU_OPTIONS = {
    "1": BasicArithmeticMenu.basic_arithmetic_menu
}
class MainMenu():
    while True:
        print(MAIN_MENU)
        choice = GeneralMethods.get_choice()
        if choice == "99":
            print("Exiting Program...")
            sys.exit()
        if choice in BASIC_MENU_OPTIONS:
            BASIC_MENU_OPTIONS[choice]()
        else:
            print("Invalid Input...")
            