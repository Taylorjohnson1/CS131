# Program: Secret Code
# Date: 10/19/2020
# Author: Taylor Johnson
# Description: To convert a message into a decimal number and then into binary
#              using a list and then converting each number within the list into
#              binary. Also to send secret codes during class to make fun of Gubanyi!

import math

def encode(message):
    '''Create a secret binary code based on a string message.'''

    ascii_code = []
    fullstr = ''

    for num in message: 
        ascii_code = ord(num)
        str = ''
        while ascii_code > 0:
            if ascii_code % 2 == 1:
                str = '1' + str
            elif ascii_code % 2 == 0:
                str = '0' + str
            ascii_code = ascii_code // 2
        print_format = '{str:0>8}'.format(str = str)
        str = print_format
        fullstr = fullstr + str

    return fullstr

def decode(message):
    '''Decodes the message the user inputs into the message varriable'''

    bin_str = message
    bin_list = []

    for i in range(0, len(bin_str), 8):
        bin_list.append(bin_str[i:i+8])

    return bin_list
    
def convert(bin_number):

    my_dec = 0
    bin_number = bin_number[::-1]

    for i in range(len(bin_number)):
        if bin_number[i] == '1':
            my_dec += math.pow(2, i)

    return my_dec

def press_enter():
    '''Allows the user to press enter at the end of a function to return to the menu'''

    input('Press Enter To Continue...')

    return main()

def introduction():
    '''introduces the program'''
    print()
    print('Secret Messages:')
    print()
    print('Do you want to send secret messages to your friends in class?')
    print('This program will convert your message into binary,')
    print('and also binary into a "secret message"!')
    print('Type in your message and it will be converted into binary!')
    print()
    print('Which of these options would you like to do?')
    print('Encode [1]         Decode [2]         Exit [3]')
    
def main():
    '''The function allows to run other fuctions and also ask the user for certian inputs.'''

    introduction()

    print()
    user_choice = input('Option:')
    print()

    # User_choice 1 calls the encoding fuction.
    if user_choice == '1':
        message = input('Encode Message:')

        print()

        encode(message)
        secret_code = encode(message)

        print('Message:',secret_code)
        print()

        press_enter()

        return main()

    # User_choice 2 calls the decoding function.
    elif user_choice == '2':
        message = input('Decode Message:')

        print()

        decode_code = decode(message)
        word = ''

        # For loop that converts decimal number into words
        for bin in decode_code:
            word = word + chr(int(convert(bin)))
        print('Message:', word)
        print()

        press_enter()

        return main()

    # User_choice 3 exits the program.
    elif user_choice == "3":
        print('Goodbye, come back again!')

        exit()

    else:
        # Gives an error if user imputs anything else other than 1, 2 or 3.
        print('ERROR: Please choose one of the options above.')

        return main()

    user_choice = main()

main()