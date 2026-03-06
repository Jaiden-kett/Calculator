from typing import List
class StatisticsAndDataAnalysisMethods:
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