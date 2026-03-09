from typing import List
class TrigonometryAndLogarthmsMethods:
    @staticmethod
    def sin(Numbers: List[float]):
        if(len(Numbers) > 2):
            print("Only accepts a list of two numbers")
            return
        else:
            opposite = Numbers[0]
            hypotenuse = Numbers[1]
            print("The length of the Opposite: ", opposite)
            print("The length of the Hypotenuse: ", hypotenuse)
            print("The sin(0) is: ",)
            sin = opposite / hypotenuse
            return sin
    @staticmethod
    def cos(Numbers: List[float]):
        if(len(Numbers) > 2):
            print("Only accepts a list of two numbers")
            return
        else:
            adjacent = Numbers[0]
            hypotenuse = Numbers[1]
            print("The length of the Opposite: ", adjacent)
            print("The length of the Hypotenuse: ", hypotenuse)
            print("The cos(0) is: ",)
            cos = adjacent / hypotenuse
            return cos
    @staticmethod
    def tan(Numbers: List[float]):
        if(len(Numbers) > 2):
            print("Only accepts a list of two numbers")
            return
        else:
            opposite = Numbers[0]
            adjacent = Numbers[1]
            print("The length of the Opposite: ", opposite)
            print("The length of the Hypotenuse: ", adjacent)
            print("The tan(0) is: ",)
            tan = opposite / adjacent
            return tan
    @staticmethod
    def inv_sin(Numbers: List[float]):
        if(len(Numbers) > 2):
            print("Only accepts a list of two numbers")
            return
        else:
            opposite = Numbers[0]
            hypotenuse = Numbers[1]
            print("The length of the Opposite: ", opposite)
            print("The length of the Hypotenuse: ", hypotenuse)
            print("The sin(0) is: ",)
            sin = opposite / hypotenuse
            inverse = TrigonometryAndLogarthmsMethods.inverse([sin])
            inverse_sin = inverse * (sin)
            return inverse_sin
    @staticmethod
    def inv_sin(Numbers: List[float]):
            sin = TrigonometryAndLogarthmsMethods.sin([Numbers])
            inverse = TrigonometryAndLogarthmsMethods.inverse([sin])
            inverse_sin = inverse * (sin)
            return inverse_sin
    @staticmethod
    def inv_cos(Numbers: List[float]):
            cos = TrigonometryAndLogarthmsMethods.cos([Numbers])
            inverse = TrigonometryAndLogarthmsMethods.inverse([cos])
            inverse_cos = inverse * (cos)
            return inverse_cos
    @staticmethod
    def inv_tan(Numbers: List[float]):
            tan = TrigonometryAndLogarthmsMethods.tan([Numbers])
            inverse = TrigonometryAndLogarthmsMethods.inverse([tan])
            inverse_tan = inverse * (tan)
            return inverse_tan

    @staticmethod
    def inverse(Numbers: List[float]):
        listOfInverse = []
        try:
            for num in Numbers:
                inverse = 1 / num
                listOfInverse.append(inverse)
        except ZeroDivisionError:
            print("cannot divide my zero")
            return
        return listOfInverse
