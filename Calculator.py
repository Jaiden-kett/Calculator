from CalculatorMethods  import CalculatorMethods
Calculator = CalculatorMethods
failSafe = True
while failSafe:

    x = input(
        "What would you like to do?\n"
        "1: Addition\n"
        "2: Subtraction\n"
        "3: Division\n"
        "4: Multiplication\n"
        "5: Remainder\n"
        "6: Power (Only first two numbers will be used)\n"
        "7: SquareRoot (only first number will be used)\n"
        "8: CubeRoot (only first number will be used)\n"
        "9: AbsoluteValue(only first number will be used)\n"
        "10: Exit\n"
    )

    if x == "10":
        break

    numbers = list(map(float, input("Enter numbers separated by space: ").split()))

    match x:
        case "1":
            print(CalculatorMethods.addition(numbers))
        case "2":
            print(CalculatorMethods.subtract(numbers))
        case "3":
            print(CalculatorMethods.divide(numbers))
        case "4":
            print(CalculatorMethods.multiply(numbers))
        case "5":
            print(CalculatorMethods.remainder(numbers))
        case "6":
            print(CalculatorMethods.power(numbers))
        case "7":
            print(CalculatorMethods.squareRoot(numbers))
        case "8":
            print(CalculatorMethods.cubeRoot(numbers))
        case "9":
            print(CalculatorMethods.abs(numbers[0]))
        case _:
            print("Invalid Input")