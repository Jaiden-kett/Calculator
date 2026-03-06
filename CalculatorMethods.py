from typing import List

class CalculatorMethods:
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
        return number[0] if number[0] >= 0 else -number[0]
    @staticmethod
    def squareRoot(numbers: float):
        n = numbers[0]
        if n < 0:
            print("Cannot calculate square root of a negative number.")
            return None
        if n == 0:
            return 0
        guess = n / 2 if n >= 1 else 1  # Start with a reasonable guess
        while CalculatorMethods.abs(guess * guess - n) > 1e-7:
            guess = 0.5 * (guess + n / guess)
        if CalculatorMethods.abs(guess - int(guess)) < 1e-7:
            return int(guess)
        return guess
    @staticmethod
    def cubeRoot(numbers: List[float]):
        n = numbers[0]
        guess = n / 3 if n >= 1 else 1
        while CalculatorMethods.abs(guess**3 - n) > 1e-7:
            guess = (2*guess + n / (guess**2)) / 3
        if CalculatorMethods.abs(guess - int(guess)) < 1e-7:
            return int(guess)
        return guess
    @staticmethod
    def max(numbers: List[float]):
        max = numbers[0]
        for nums in numbers:
            if nums > max:
                max = nums
        return max
    @staticmethod
    def min(numbers: List[float]):
        min = numbers[0]
        for nums in numbers:
            if nums < min:
                min = nums
        return min
    @staticmethod 
    def divisors(number):
        divisors = []
        for i in range(1, number + 1):
            if number % i == 0:
                divisors.append(i)
        return divisors
    @staticmethod
    def greatestCommonDivisor(numbers: List[float]):
        max_divisor = 1
        firstNumber = int(numbers[0])
        secondNumber = int(numbers[1])
        if firstNumber < 1 or secondNumber < 1:
            print("Both numbers must be over one to find greatest common divisor")
            return None
        
        firstNumberDivisors = CalculatorMethods.divisors(firstNumber)
        secondNumberDivisors = CalculatorMethods.divisors(secondNumber)  
        print("this is the divisors")
        print(firstNumberDivisors)
        print(secondNumberDivisors)

        for d1 in firstNumberDivisors:
            for d2 in secondNumberDivisors:
                if d1 == d2:
                    if d1 > max_divisor:
                        max_divisor = d1
        if max_divisor == 1:
            print("There are no common divisors over one")
            return None
        else:
            return max_divisor
    @staticmethod
    def leastCommonMultiple(numbers: List[float]):
        firstMultiple = numbers[0]
        secondMultiple = numbers[1]
        while(firstMultiple != secondMultiple):
            while(firstMultiple < secondMultiple):
                firstMultiple += numbers[0]
            while(secondMultiple < firstMultiple):
                secondMultiple += numbers[1]
        return firstMultiple
    @staticmethod
    def factorial(numbers: List[float]):
        total = 1
        for i in range(1,int(numbers[0]+1)):
            total *= i
        return total
    