class GeneralMethods:
    def get_numbers():
        user_input = input("Enter numbers seperated by spaces: ")
        return [float(x) for x in user_input.split()]
    def get_choice():
        user_input = input("Enter choice: ")
        return user_input
    def menu_functions(MENU, operations):
        while True:
            print(MENU)
            choice = GeneralMethods.get_choice()
            if choice == "99":
                break
            if choice in operations:
                numbers = GeneralMethods.get_numbers()
                result = operations[choice](numbers)
                print("Result: ", result)
            else:
                print("Invalid Input... ")