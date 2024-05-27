#Importing the random module
import random

#Generate a random number between 1 and 10
secret_number= random.randint(1,10)

#Maximum attempts allowed
max_attempts=3

#Function to display a welcome message
def welcome_message():
    print("\nWelcome to the Number Guessing Game! ")
    print(f"You have {max_attempts} attempts to guess the correct number.")

#Function for Recursive guessing
def guess_recursive(attempts_left):
    #Get User input
    guess=int(input("\nGuess the number (between 1 and 10):"))

    #Check if the guess is correct
    if guess==secret_number:
        print("Congratulations! You guesses the correct number!")
    else:
        print(f"Wrong guess. Attempts left:{attempts_left-1}")
        if attempts_left>1:
            #Make a recursive call for another guess
            guess_recursive(attempts_left - 1)
        else:
            print(f"\nSorry, you couldn't guess the number. The correct number was {secret_number}.")

# Calling for the finction
welcome_message()
guess_recursive(max_attempts)

#Using id() to get memory addresses
print(f"Memory address of secret number {secret_number} is: {id(secret_number)}")






# Exercise
def find_first_repeating_character(s):
    char_count = {}
    for char in s:
        # Check if the character is already in the dictionary
        if char in char_count:
            # If it's already there, print the character and its memory address
            print(f"First repeating character: {char}, Memory address: {id(char)}")
            return char, id(char)
        else:
            # If not, add it to the dictionary with a count of 1
            char_count[char] = 1
    
    # If no repeating character is found, return None
    return None

# Example usage:
string = "abcdefgabc"
result = find_first_repeating_character(string)
if result is None:
    print("No repeating character found.")






                           