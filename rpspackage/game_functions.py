import random
# random variable generator

# created five functions - get user response, convert, get computer response, convert, compare both values and determine winner, play again?
def retrieve_user_response():
    """
    This function uses a list to validate the user's response.
    The user is prompted to enter R,P or S
    :return: user_response
    # a docstring explains the purpose of a function
    """
    user_options = ['R', 'P','S']
    # The list shows the valid options of the user
    while True:
        user_response = input("Please select R, P or S: ").upper()
        # input function returns outputs value entered by the user and converts it to uppercase
        if user_response in user_options:
            return user_response
# The loop ensures the user enters a valid response
# conditional statement - function only returns the user response if it's within the sequence of valid options
# continuously prompts user until valid answer is entered


def convert_user_response(user_response):
    """
    This function uses a dictionary to convert the letter inputted by the user into the full word representation
    :param user_response:
    :return: string - converted response
    """
    user_choice = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    return user_choice[user_response]
# returns the corresponding word - looking up the key (user_response) and its value - the converted word

def retrieve_computer_response():
    return random.randint(0, 2)
    # computer generates random number between both integers

def convert_computer_response(computer_response):
    """
    This function uses a dictionary to convert the randomised integer into a string
    :param computer_response:
    :return: converted computer response
    """
    computer_choice = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}
    return computer_choice[computer_response]
# returns the corresponding word - looking up the key (computer_response) and its value - the converted word

def determine_winner(user_response, computer_choice):
    """
    This function uses a dictionary and conditional statement to compare both values and determine the winner
    :param user_response:
    :param computer_choice:
    :return: results

    """
    outcomes = {"Rock": "Scissors", "Paper": "Rock","Scissors": "Paper"}

    # dictionary {} outlines the different outcomes
    # keys = user choice/value = what option can the user beat?
    # keys are IMMUTABLE - useful for the game as the three items being played never change

    if user_response == computer_choice:
        return "It's a draw!"
    # if both values are equal to each other (equality operator)
    elif outcomes[user_response] == computer_choice:
        return "You win!"
    # [] looks up the key in the dictionary, if the value is = to the computer's choice, the user wins
    # if the key does not match up to the computer's choice, the user loses
    else:
        return "You lose!"

def play_again():
    """
    This function asks the user if they want to play again.
    :return: boolean - Returns True for Yes, False for No.
    """
    while True:
        user_input = input("\nDo you want to play again? (Y/N): ").upper()
        if user_input == "Y":
            return True
        elif user_input == "N":
            return False
        return None
# loop ensures a valid response
# true/false - Y/N break exits loop allowing game to proceed/end
# invalid answer - returns None (prompts user in game)
