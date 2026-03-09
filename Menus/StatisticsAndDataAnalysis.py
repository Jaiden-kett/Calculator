from Methods.StatisticsAndDataAnalysis import StatisticsAndDataAnalysisMethods
from Methods.General import GeneralMethods
MENU = """
What function would you like to use
|—— 1: Maximum
|—— 2: Minimum
|—— 3: Mean
|—— 4: Median
|—— 5: Mode
|—— 6: Standard Deviation
|—— 7: Variance
|—— 8: Range
|—— 99: Back
"""

operations = {
    "1": StatisticsAndDataAnalysisMethods.max,
    "2": StatisticsAndDataAnalysisMethods.min,
    "3": StatisticsAndDataAnalysisMethods.mean,
    "4": StatisticsAndDataAnalysisMethods.median,
    "5": StatisticsAndDataAnalysisMethods.mode,
    "6": StatisticsAndDataAnalysisMethods.standard_deviation,
    "7": StatisticsAndDataAnalysisMethods.variance,
    "8": StatisticsAndDataAnalysisMethods.range
}

def statistics_and_data_analysis_menu():
    GeneralMethods.menu_functions(MENU, operations)