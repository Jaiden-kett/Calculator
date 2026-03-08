from typing import List
class GeneralMethods:
    def get_numbers():
        user_input = input("Enter numbers seperated by spaces: ")
        return [float(x) for x in user_input.split()]
    def get_choice():
        user_input = input("Enter choice: ")
        return user_input
    