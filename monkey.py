# Problem: Monkey Buisness
# Date: October 7th 2020
# Author: Taylor Johnson
# Description: This is Code that solves the monkey problem by searching a 
#              wide range of numbers that the user can choice to search from.

def introduction():
    #Introduction to the program
    print('Monkey Problem!')
    print()
    print('What is the Monkey Problem?')
    print()
    print('Description: These 5 sailors have a pile of coconuts.')
    print('Then the five sailors go to bed. The first sailor wakes')
    print('up and divids the pile by five, he has a remainder of one and gives it to the monkey.')
    print('The first sailor goes back to bed and takes his share of coconuts.')
    print('The second sailor does the same thing, divides the')
    print('coconuts and has a remainder of two and gives it to the monkey.')
    print('The second sailor goes to bed and takes his share of coconuts.')
    print('The third sailor wakes up and divids the pile again and has a remainder')
    print('of three. Gives the remainder to the monkey.')
    print('He goes to bed and takes his share. The forth sailor wakes up and') 
    print('divides the pile of coconuts and has a remainder of four.')
    print('The forth sailor give the remainder to the monkey and takes his')
    print('share and goes to bed. The fifth sailor wakes up')
    print('and divides the pile agian and has a remainder of zero.')
    print('The fifth sailor takes his share and goes to bed.')
    print('In the morning, Everyone wakes back up and and divides')
    print('the pile one last time. They have a remainder of one.')
    print('They give the one coconut to the monkey and they go on there way.')
    print()
    print('How many coconuts are in the orignal pile?')
    print()
    print('Every Solution to The Monkey Problem:')
    print('What range of numbers would you like to search?')

def choice(originali, answer):
    if answer == '1':
        print(originali)
    elif answer == '0':
        exit

def is_a_solution(one, two):
    '''This function determains weither or not a number will work.
    If the number does not have a certain number after being divided
    then the number will not work.'''

    # The varriable I is every number that the range will be searching
    # between the varriables one and two that the user inputs.
    answer = input('Would you like to print out the outputs? yes(1) / no(0):')
    for i in range(one, two):
        originali = i
        # First Sailor:
        if i % 5 == 1:
            i = i // 5 * 4
            # Second Sailor:
            if i % 5 == 2:
                i = i // 5 * 4
                # Third Sailor:
                if i % 5 == 3:
                    i = i // 5 * 4
                    # Forth Sailor:
                    if i % 5 == 4:
                        i = i // 5 * 4
                        # Fifth Sailocr:
                        if i % 5 == 0:
                            i = i // 5 * 4
                            # Last division remainder must be 1:
                            if i % 5 == 1:
                                choice(originali, answer)                                
def main():
    '''The function allows to run other fuctions and with the import time
    allows us to recieve a time on how quickly the computer can figure
    out how many solutions are within a certain range.'''

    import time

    introduction()

    # User Inputs:
    one = int(input('Input First Number:'))
    two = int(input('Input Second Number:'))

    start_t = time.time()
    start_c = time.clock()

    is_a_solution(one, two)

    end_t = time.time()
    end_c = time.clock()

    # The amount of actual, real-time, seconds.
    wall_time = end_t - start_t
    # CPU time is less than real-time, it's the amount of time the computer
    # processor spends working on the specific task.
    cpu_time = end_c - start_c

    print('Wall Time:', wall_time)
    print('CPU Time', cpu_time)

main()