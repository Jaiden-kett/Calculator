from typing import List
class PowerAndRootsMethods:
    @staticmethod
    def power(nums: List[float]):
        total = nums[0]
        for num in nums[1:]:
            total = total ** num
        return total    
    @staticmethod
    def square_root(nums: List[float]):
        return [n ** (1/2) for n in nums]
    @staticmethod
    def cube_root(nums: List[float]):
        return [n ** (1/3) for n in nums]    
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