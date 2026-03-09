from Menus.BasicArithmetic import basic_aritmetic_menu
from Menus.PowersAndRoots import power_and_roots_menu
from Menus.NumberTheory import number_theory_menu
from Menus.StatisticsAndDataAnalysis import statistics_and_data_analysis_menu
from Methods.General import GeneralMethods
MAIN_MENU = """
What type of Calculator would you like to use?
|—— 1. Basic Arithmetic
|—— 2. Power & Roots
|—— 3. Number Theory
|—— 4. Statistics & Data Analysis
|—— 5. Trigonometry & Logarithms (In Progress)
|—— 6. Bitwise / Programmer Functions (Coming soon)
|—— 7. Memory Functions (Coming soon)
|—— 8. Number Utilities (Coming soon)
|—— 9. Unit Conversions (Coming soon)
|—— 10. Advanced Features (Coming soon)
|—— 99. Exit
"""
operations = {
    "1": basic_aritmetic_menu,
    "2": power_and_roots_menu,
    "3": number_theory_menu,
    "4": statistics_and_data_analysis_menu
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
            