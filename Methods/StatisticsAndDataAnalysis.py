from typing import List
class StatisticsAndDataAnalysisMethods:
    @staticmethod
    def max(nums: List[float]):
        max = nums[0]
        for nums in nums:
            if nums > max:
                max = nums
        return max
    @staticmethod
    def min(nums: List[float]):
        min = nums[0]
        for nums in nums:
            if nums < min:
                min = nums
        return min