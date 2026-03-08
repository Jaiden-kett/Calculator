from typing import List
class BasicArithmeticMethods:
    @staticmethod
    def addition(numbers: List[float]):
        returnValue = 0
        for num in numbers:
            returnValue += num
        return returnValue
    @staticmethod
    def subtract(numbers: List[float]):
        returnValue = numbers[0]
        for i in range(1, len(numbers)):
            returnValue -= numbers[i]
        return returnValue
    @staticmethod
    def divide(numbers: List[float]):
        returnValue = numbers[0]
        for i in range(1, len(numbers)):
            try:
                returnValue /= numbers[i]
            except ZeroDivisionError:
                print("Division by 0 is not allowed... Task Failed...")
                return None
        return returnValue
    @staticmethod
    def multiply(numbers: List[float]):
        returnValue = numbers[0]
        for i in range(1, len(numbers)):
            returnValue *= numbers[i]
        return returnValue
    @staticmethod
    def remainder(numbers: List[float]):
        returnValue = numbers[0]
        for i in range(1, len(numbers)):
            try:
                returnValue %= numbers[i]
            except ZeroDivisionError:
                print("Division by 0 is not allowed... Task Failed...")
        return returnValue
