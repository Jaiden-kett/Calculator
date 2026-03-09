from Methods.PowerAndRoots import PowerAndRootsMethods
from Methods.General import GeneralMethods
MENU = """
What function would you like to use
|—— 1: Power
|—— 2: Square Root
|—— 3: Cube Root
|—— 4: Factorial
|—— 5: Absolute Value
|—— 99: Back
"""

operations = {
"1": PowerAndRootsMethods.power,
"2": PowerAndRootsMethods.square_root,
"3": PowerAndRootsMethods.cube_root,
"4": PowerAndRootsMethods.factorial,
"5": PowerAndRootsMethods.abs,
}

def power_and_roots_menu():
    GeneralMethods.menu_functions(MENU, operations)