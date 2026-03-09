from Methods.TrigonometryAndLogarithms import TrigonometryAndLogarthmsMethods
from Methods.General import GeneralMethods
MENU = """
What function would you like to use
|—— 1: Sin
|—— 2: Cosine
|—— 3: Tangent
|—— 4: Inverse Sine (arcsin)
|—— 5: Inverse cosine (arccos)
|—— 6: Inverse tangent (arctan)
|—— 7: Logarithm (base 10)
|—— 8: Natural logarithm (ln)
|—— 6: Exponential (e^x)
|—— 99: Back
"""

operations = {
    "1": TrigonometryAndLogarthmsMethods.sin,
    "2": TrigonometryAndLogarthmsMethods.cos,
    "3": TrigonometryAndLogarthmsMethods.tan
}
@staticmethod
def trigonometry_and_logarithms_menu():
    GeneralMethods.menu_functions(MENU, operations)