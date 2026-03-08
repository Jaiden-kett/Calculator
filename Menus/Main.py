from Menus.BasicArithmetic import basic_aritmetic_menu
from Menus.PowersAndRoots import power_and_roos_menu
from Methods.General import GeneralMethods
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
operations = {
    "1": basic_aritmetic_menu,
    "2": power_and_roos_menu
}
class MainMenu():
    while True:
        print(MAIN_MENU)
        choice = GeneralMethods.get_choice()
        if choice == "99":
            print("Exiting Program...")
            break
        if choice in operations:
            operations[choice]()
        else:
            print("Invalid Input...")
            