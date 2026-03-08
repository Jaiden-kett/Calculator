from typing import List
class PowerAndRootsMethods:
    @staticmethod
    def power(nums: List[float]):
        total = nums[0]
        for i in range(1,int(nums[1])):
            total *= nums[0]
        return total
    @staticmethod
    def squareRoot(nums: List[float]):
        returnList = []
        for i in nums:
            if i < 0:
                print("Cannot calculate square root of a negative number.")
                returnList.append(None)
            if i == 0:
                returnList.append(0)
            guess = i / 2 if i >= 1 else 1
            while PowerAndRootsMethods.abs([guess * guess - i])[0] > 1e-7:
                guess = 0.5 * (guess + i / guess)
            if PowerAndRootsMethods.abs([guess - int(guess)])[0] < 1e-7:
                returnList.append(int(guess))
        return returnList  
    @staticmethod
    def cubeRoot(nums: List[float]):
        returnList = []
        for i in nums:
            guess = i / 3 if i >= 1 else 1
            while PowerAndRootsMethods.abs([guess**3 - i])[0] > 1e-7:
                guess = (2*guess + i / (guess**2)) / 3
            if PowerAndRootsMethods.abs([guess - int(guess)])[0] < 1e-7:
                returnList.append(int(guess))
        return returnList
    @staticmethod
    def factorial(nums: List[float]):
        returnList = []
        for i1 in range(0,len(nums)):
            total = 1
            for i2 in range(2,int(nums[i1]+1)):
                total *= i2
            returnList.append(total)
        return returnList
    @staticmethod
    def abs(nums: List[float]):
        returnList = []
        for i in nums:
            returnList.append(i if i >= 0 else -i)
        return returnList