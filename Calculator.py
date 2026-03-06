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
        "7: Exit\n"
    )

    if x == "7":
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
        case _:
            print("Invalid option")