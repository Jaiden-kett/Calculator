from typing import List

class Calculator:
    @staticmethod
    def addition(numbers: List[float]):
        total = 0
        for num in numbers:
            total += num
        return total

    @staticmethod
    def subtract(numbers: List[float]):
        total = numbers[0]
        for i in range(len(numbers) - 1):
            total -= numbers[i + 1]
        return total

    @staticmethod
    def divide(numbers: List[float]):
        total = numbers[0]
        for i in range(len(numbers) - 1):
            try:
                total /= numbers[i + 1]
            except ZeroDivisionError:
                print("Division by 0 is not allowed... Task Failed...")
                return None
        return total

    @staticmethod
    def multiply(numbers: List[float]):
        total = numbers[0]
        for i in range(len(numbers) - 1):
            total *= numbers[i + 1]
        return total

    @staticmethod
    def remainder(numbers: List[float]):
        total = numbers[0]
        for i in range(len(numbers) - 1):
            try:
                total %= numbers[i + 1]
            except ZeroDivisionError:
                print("Division by 0 is not allowed... Task Failed...")
                return None
        return total
    
    @staticmethod
    def power(numbers: List[float]):
        root = numbers[0]
        power = int(numbers[1])
        total = root
        for i in range(power):
            print("current total:")
            print(total)
            print("current integration ")
            print(i)
            total *= power
        return total/ power

    @staticmethod
    def abs(number: List[float]):
        return number if number >= 0 else -number
    
    @staticmethod
    def squareRoot(numbers: float):
        n = numbers[0]
        if n < 0:
            print("Cannot calculate square root of a negative number.")
            return None
        if n == 0:
            return 0
        guess = n / 2 if n >= 1 else 1  # Start with a reasonable guess
        while Calculator.abs(guess * guess - n) > 1e-7:
            guess = 0.5 * (guess + n / guess)
        if Calculator.abs(guess - int(guess)) < 1e-7:
            return int(guess)
        return guess

    @staticmethod
    def cubeRoot(numbers: List[float]):
        n = numbers[0]
        guess = n / 3 if n >= 1 else 1
        while Calculator.abs(guess**3 - n) > 1e-7:
            guess = (2*guess + n / (guess**2)) / 3
        if Calculator.abs(guess - int(guess)) < 1e-7:
            return int(guess)
        return guess
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
            print(Calculator.addition(numbers))
        case "2":
            print(Calculator.subtract(numbers))
        case "3":
            print(Calculator.divide(numbers))
        case "4":
            print(Calculator.multiply(numbers))
        case "5":
            print(Calculator.remainder(numbers))
        case "6":
            print(Calculator.power(numbers))
        case "7":
            print(Calculator.squareRoot(numbers))
        case "8":
            print(Calculator.cubeRoot(numbers))
        case "9":
            print(Calculator.abs(numbers[0]))
        case _:
            print("Invalid Input")