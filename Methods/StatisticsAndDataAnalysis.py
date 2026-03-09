from typing import List
from Methods.BasicArithmetic import BasicArithmeticMethods
from Methods.PowerAndRoots import PowerAndRootsMethods

class StatisticsAndDataAnalysisMethods:

    @staticmethod
    def max(nums: List[float]):
        maximum = nums[0]
        for num in nums:
            if num > maximum:
                maximum = num
        return maximum

    @staticmethod
    def min(nums: List[float]):
        minimum = nums[0]
        for num in nums:
            if num < minimum:
                minimum = num
        return minimum

    @staticmethod
    def mean(nums: List[float]):
        return BasicArithmeticMethods.add(nums) / len(nums)

    @staticmethod
    def median(nums: List[float]):
        nums = StatisticsAndDataAnalysisMethods.sort(nums.copy())
        n = len(nums)

        if n % 2 == 0:
            mid1 = nums[n // 2]
            mid2 = nums[n // 2 - 1]
            return StatisticsAndDataAnalysisMethods.mean([mid1, mid2])
        else:
            return nums[n // 2]

    @staticmethod
    def mode(nums: List[float]):
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        max_count = max(counts.values())
        return [num for num, count in counts.items() if count == max_count]

    @staticmethod
    def sort(nums: List[float]):
        n = len(nums)

        for i in range(n):
            swapped = False

            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True

            if not swapped:
                break

        return nums

    @staticmethod
    def variance(nums: List[float]):
        mean = StatisticsAndDataAnalysisMethods.mean(nums)

        total = 0
        for num in nums:
            total += (num - mean) ** 2

        return total / (len(nums) - 1)

    @staticmethod
    def standard_deviation(nums: List[float]):
        variance = StatisticsAndDataAnalysisMethods.variance(nums)
        return variance ** 0.5

    @staticmethod
    def range(nums: List[float]):
        return (StatisticsAndDataAnalysisMethods.max(nums)
                - StatisticsAndDataAnalysisMethods.min(nums))