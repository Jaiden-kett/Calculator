from typing import List
class BasicArithmeticMethods:
    @staticmethod
    def addition(numbers: List[float]):
        sum = 0
        for num in numbers:
            sum += num
        return sum
    @staticmethod
    def subtract(numbers: List[float]):
        total = numbers[0]
        for i in range(1, len(numbers)):
            total -= numbers[i]
        return total
    @staticmethod
    def divide(numbers: List[float]):
        total = numbers[0]
        for i in range(1, len(numbers)):
            try:
                total /= numbers[i]
            except ZeroDivisionError:
                print("Division by 0 is not allowed... Task Failed...")
                return None
        return total
    @staticmethod
    def multiply(numbers: List[float]):
        total = numbers[0]
        for i in range(1, len(numbers)):
            total *= numbers[i]
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
