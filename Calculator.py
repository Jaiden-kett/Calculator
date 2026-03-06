#from Methods.AdvancedFeaturesMethods import AdvancedFeaturesMethods
from Methods.BasicArithmeticMethods import BasicArithmeticMethods
#from Methods.BitewiseAndProgrammerFunctionsMethods import BitewiseAndProgrammerFunctionsMethods
#from Methods.MemoryFunctionsMethods import MemoryFunctionsMethods
from Methods.NumberTheoryMethods import NumberTheoryMethods
#from Methods.NumberUtilitiesMethods import NumberUtilitiesMethods
from Methods.PowerAndRootsMethods import PowerAndRootsMethods
from Methods.StatisticsAndDataAnalysisMethods import StatisticsAndDataAnalysisMethods
#from Methods.TrigonometryAndLogarithmsMethods import TrigonometryAndLogarithmsMethods
class Calculator:
    while True:
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
        BASIC_ARITHMETIC_MENU = """
        What function would you like to use
        |—— 1: Addition
        |—— 2: Subtraction
        |—— 3: Multiplication
        |—— 4: Division
        |—— 5: Remainder
        |—— 99: Back
        """
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
    
        print(MAIN_MENU)
        inputMainMenu = input("Enter choice: ")

        if inputMainMenu == "99":
            print("Exiting calculator...")
            break

        match inputMainMenu:
            case "1":
                print(BASIC_ARITHMETIC_MENU)
                inputBasicArithmeticMenu = input("Enter choice: ")
                if inputBasicArithmeticMenu == "99":
                    print("Exiting calculator...")
                    break
                match inputBasicArithmeticMenu:
                    case "1":
                        user_input = input("Enter numbers separated by spaces: ")
                        numbers = [float(x) for x in user_input.split()]
                        print(BasicArithmeticMethods.addition(numbers))

            case "2":
                print(POWERS_AND_ROOTS_MENU)
                inputPowersAndRootsMenu = input("Enter choice: ")
                if inputPowersAndRootsMenu == "99":
                    print("Exiting calculator...")
                    break
            case "3":
                print(NUMBER_THEORY_MENU)
                inputNumberTheoryMeny = input("Enter choice: ")
                if inputNumberTheoryMeny == "99":
                    print("Exiting calculator...")
                    break
            case "4":
                print(STATISTICS_MENU)
                inputStatisticsMenu = input("Enter choice: ")
                if inputStatisticsMenu == "99":
                    print("Exiting calculator...")
                    break
            case "5":
                print(TRIGONOMETRY_AND_LOGARITHMS_MENU)
                inputTrigonometryAndLogarithmsMenu = input("Enter choice: ")
                if inputTrigonometryAndLogarithmsMenu == "99":
                    print("Exiting calculator...")
                    break
            case "6":
                print(BITEWISE_PROGRAMMER_FUNCTIONS_MENU)
                inputBitewiseProgrammerFunctionsMenu = input("Enter choice: ")
                if inputBitewiseProgrammerFunctionsMenu == "99":
                    print("Exiting calculator...")
                    break
            case "7":
                print(MEMORY_FUNCTIONS_MENU)
                inputMemoryFunctionsMenu = input("Enter choice: ")
                if inputMemoryFunctionsMenu == "99":
                    print("Exiting calculator...")
                    break
            case "8":
                print(NUMBER_UTILITIES_MENU)
                inputNumberUtilitiesMenu = input("Enter choice: ")
                if inputNumberUtilitiesMenu == "99":
                    print("Exiting calculator...")
                    break
            case "9":
                print(UNIT_CONVERSIONS_MENU)
                inputUnitConversionsMenu = input("Enter choice: ")
                if inputUnitConversionsMenu == "99":
                    print("Exiting calculator...")
                    break
            case "10":
                print(ADVANCED_FEATURES_MENU)
                inputAdvancedFeaturesMenu = input("Enter choice: ")
                if inputAdvancedFeaturesMenu == "99":
                    print("Exiting calculator...")
                    break
            case _:
                print("Invalid input")
                break