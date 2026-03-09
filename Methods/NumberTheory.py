from typing import List
class NumberTheoryMethods:
    @staticmethod
    def divisors(numbers: List[int]):
        results = []
        for n in numbers:
            divisors = []
            for i in range(1, int(n)):
                if n % i == 0:
                    divisors.append(i)
            results.append(divisors)

        return results    
    @staticmethod
    def gcdTwoNumbers(a, b):
        while b != 0:
            a, b = b, a % b
        return a    
    @staticmethod
    def greatestCommonDivisor(nums: List[int]):
        gcd_value = nums[0]
        for i in range(1, len(nums)):
            gcd_value = NumberTheoryMethods.gcdTwoNumbers(gcd_value, nums[i])
        return gcd_value
    @staticmethod
    def leastCommonMultiple(nums: List[float]):
        multiples = nums.copy()
        while not all(x == multiples[0] for x in multiples):
            for i in range(len(multiples)-1):
                while(multiples[i] < multiples[i+1]):
                    multiples[i] += nums[i]
                while(multiples[i+1] < multiples[i]):
                    multiples[i+1] += nums[i+1]
        return multiples[0]
