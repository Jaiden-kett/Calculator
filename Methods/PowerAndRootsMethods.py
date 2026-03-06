from typing import List
class PowerAndRootsMethods:
    @staticmethod
    def power(numbers: List[float]):
        total = numbers[0]
        for i in range(1,int(numbers[1])):
            total *= numbers[0]
        return total
    @staticmethod
    def squareRoot(numbers: List[float]):
        returnList = []
        for i in numbers:
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
    def cubeRoot(numbers: List[float]):
        returnList = []
        for i in numbers:
            guess = i / 3 if i >= 1 else 1
            while PowerAndRootsMethods.abs([guess**3 - i])[0] > 1e-7:
                guess = (2*guess + i / (guess**2)) / 3
            if PowerAndRootsMethods.abs([guess - int(guess)])[0] < 1e-7:
                returnList.append(int(guess))
        return returnList
    @staticmethod
    def factorial(numbers: List[float]):
        returnList = []
        for i1 in range(0,len(numbers)):
            total = 1
            for i2 in range(2,int(numbers[i1]+1)):
                total *= i2
            returnList.append(total)
        return returnList
    @staticmethod
    def abs(number: List[float]):
        returnList = []
        for i in number:
            returnList.append(i if i >= 0 else -i)
        return returnList