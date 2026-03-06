from typing import List
class NumberTheoryMethods:
    @staticmethod
    def divisors(number):
        divisors = []
        for i in range(1, number + 1):
            if number % i == 0:
                divisors.append(i)
        return divisors
    @staticmethod
    def gcdTwoNumbers(a, b):
        while b != 0:
            a, b = b, a % b
        return a    
    @staticmethod
    def greatestCommonDivisor(numbers: List[int]):
        gcd_value = numbers[0]
        for i in range(1, len(numbers)):
            gcd_value = NumberTheoryMethods.gcdTwoNumbers(gcd_value, numbers[i])
        return gcd_value
    @staticmethod
    def leastCommonMultiple(numbers: List[float]):
        multiples = numbers.copy()
        while not all(x == multiples[0] for x in multiples):
            for i in range(len(multiples)-1):
                while(multiples[i] < multiples[i+1]):
                    multiples[i] += numbers[i]
                while(multiples[i+1] < multiples[i]):
                    multiples[i+1] += numbers[i+1]
        return multiples[0]
