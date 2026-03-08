from typing import List
class BasicArithmeticMethods:
    @staticmethod
    def add(nums: List[float]):
        returnValue = 0
        for num in nums:
            returnValue += num
        return returnValue
    @staticmethod
    def subtract(nums: List[float]):
        returnValue = nums[0]
        for i in range(1, len(nums)):
            returnValue -= nums[i]
        return returnValue
    @staticmethod
    def divide(nums: List[float]):
        returnValue = nums[0]
        for i in range(1, len(nums)):
            try:
                returnValue /= nums[i]
            except ZeroDivisionError:
                print("Division by 0 is not allowed... Task Failed...")
                return None
        return returnValue
    @staticmethod
    def multiply(nums: List[float]):
        returnValue = nums[0]
        for i in range(1, len(nums)):
            returnValue *= nums[i]
        return returnValue
    @staticmethod
    def remainder(nums: List[float]):
        returnValue = nums[0]
        for i in range(1, len(nums)):
            try:
                returnValue %= nums[i]
            except ZeroDivisionError:
                print("Division by 0 is not allowed... Task Failed...")
        return returnValue
