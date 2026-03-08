from Menus.MainMenu import MainMenu
class Calculator:
    while True:
        POWERS_AND_ROOTS_MENU = """
        What function would you like to use
        |—— 1: Power
        |—— 2: Square Root
        |—— 3: Cube Root
        |—— 4: Factorial
        |—— 5: Absolute Value
        |—— 99: Back
        """
        NUMBER_THEORY_MENU = """
        What function would you like to use
        |—— 1: Greatest Common Divisor
        |—— 2: Least Common Multiple
        |—— 3: Divisors
        |—— 99: Back
        """
        STATISTICS_MENU = """
        What function would you like to use
        |—— 1: Maximum
        |—— 2: Minimum
        |—— 3: Mean
        |—— 4: Median
        |—— 5: Mode
        |—— 6: Standard Deviation
        |—— 7: Variance
        |—— 8: Range
        |—— 99: Back
        """
        TRIGONOMETRY_AND_LOGARITHMS_MENU = """
        What function would you like to use
        |—— 1: Sin
        |—— 2: Cosine
        |—— 3: Tangent
        |—— 4: Inverse Sine (arcsin)
        |—— 5: Inverse cosine (arccos)
        |—— 6: Inverse tangent (arctan)
        |—— 7: Logarithm (base 10)
        |—— 8: Natural logarithm (ln)
        |—— 6: Exponential (e^x)
        |—— 99: Back
        """
        BITEWISE_PROGRAMMER_FUNCTIONS_MENU = """
        What function would you like to use
        |—— 1: AND
        |—— 2: OR
        |—— 3: XOR
        |—— 4: NOT
        |—— 99: Back
        """
        MEMORY_FUNCTIONS_MENU = """
        What function would you like to use
        |—— 1: Memory store
        |—— 2: Memory recall
        |—— 3: Memory add
        |—— 4: Memory subtract
        |—— 5: Memory clear
        |—— 99: Back
        """
        NUMBER_UTILITIES_MENU = """
        What function would you like to use
        |—— 1: Prime number check
        |—— 2: Prime factorization
        |—— 3: Even/odd check
        |—— 4: Fibonacci number
        |—— 99: Back
        """
        UNIT_CONVERSIONS_MENU = """
        What function would you like to use
        |—— 1: Celsius ↔ Fahrenheit
        |—— 2: Miles ↔ Kilometers
        |—— 3: Pounds ↔ Kilograms
        |—— 4: Degrees ↔ Radians
        |—— 99: Back
        """
        ADVANCED_FEATURES_MENU = """
        What function would you like to use
        |—— 1: Expression parsing
        |—— 2: Parentheses support
        |—— 3: History of calculations
        |—— 4: Undo last calculation
        |—— 5: Graphing functions
        |—— 6: Matrix calculations
        |—— 99: Back
        """
        MainMenu()