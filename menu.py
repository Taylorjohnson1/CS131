#Project: Menu-Driven
#Date: 9/10/2020
#Author: Taylor Johnson
#Description: Creating a Menu-Driven program that can
#             perfrom tasks based on what the user inputs.

def addition():
    '''Takes two floats that users inputs into the program and adds them together'''
    print()
    print('Adding Numbers')
    print()
    var = float(input("Please Input A Number:"))
    var2 = float(input("Please Input Another Number:"))
    answer_add = var + var2
    print(var, '+', var2, '=', '{:.2f}'.format(answer_add))

def subtraction():
    '''Takes two floats that the user inputs into the program and subtracts them to get the output'''
    print()
    print('Subtracting Numbers')
    var = float(input('Please Input A Number:'))
    var2 = float(input('Please Input Another Number:'))
    answer_sub = var - var2
    print(var, '-', var2, '=', '{:.2f}'.format(answer_sub))

def multiply():
    '''Takes two floats that the user inputs into the program and multiplys them to get the output'''
    print()
    print('Multiplying Numbers')
    print()
    var = float(input('Please Input A Number:'))
    var2 = float(input('Please Input Another Number:'))
    answer_mult = var * var2
    print(var, '*', var2, '=', '{:.2f}'.format(answer_mult))

def divide():
    '''Takes two floates that the user inputs into the program and divides them to get the output '''
    print()
    print('Dividing Numbers')
    print()
    var = float(input('Please Input A Number:'))
    var2 = float(input('Please Input Another Number:'))
    answer_div = (var / var2)
    print(var, '/', var2, '=', '{:.2f}'.format(answer_div))

def menu():
    '''The menu for the program that prints out after every loop'''
    print()
    print('Menu-Driven Calculator:')
    print()
    print("Choose an option with the corresponding number in the ().")
    print("Addition (1)    Subtraction (2)    Multiply (3)    Divide (4)    Quit (5)")
    selection = input('Please Select One: ')
    return selection

def press_enter():
    '''Allows the user to press enter at the end of a function to return to the menu'''
    input('Press Enter To Continue...')

#Main Fuction
#Description: The main fuction defines if the user inputs the
#             number 1 it will execute the Addition fuction and
#             so on and so forth until the user inputs 5, then
#             the program quits.
def main():
    '''While loop that speficies if the user inputs a number then the function would be executed'''
    user_choice = menu()
    while user_choice != '5':
        if user_choice == '1':
            addition()
            press_enter()
        if user_choice == '2':
            subtraction()
            press_enter()
        if user_choice == '3':
            multiply()
            press_enter()
        if user_choice == '4':
            divide()
            press_enter()
        user_choice = menu()
    print()
    print('Goodbye')
    print()
main()


