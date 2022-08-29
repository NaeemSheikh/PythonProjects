# Project 01 - Number Guessing Game
import random

def number_input(s):
    '''
    A function that takes number input from the user and converts it into an integer, 
    returning the value.
    If the input is not an integer, it prompts user to try again with a valid input and
    calls itself until a valid input is received.
    '''
    try:
        number = int(input(s))
    except:
        print("Incorrect value entered. Please enter a number:")
        number = number_input(s)
    return number

print("NUMBER GUESSING GAME\n")
print("Enter a range of numbers to guess from")

# User input lower & upper range of integers to guess from
LOWER = number_input("Enter the lower number: ")
UPPER = number_input("Enter the upper number: ")

# Program randomly selects a number in the given range
TARGET = random.randint(LOWER, UPPER)
print("\nNumber selected. GAME START!")

# User repeatedly tries to guess number with hints of too high/low
count = 0
guess = None

while guess != TARGET:
    guess = number_input("Enter a number: ")
    count += 1
    if guess > TARGET:
        print(f"{guess} is too high. Try again:")
    elif guess < TARGET: 
        print(f"{guess} is too low. Try again:")

# Program congratulates User for guessing number in N number of tries.
print(f"\nYOU WIN! You guessed the number {TARGET} in {count} tries!")