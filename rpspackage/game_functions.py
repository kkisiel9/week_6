import random
# import module: random variable generator

# created five functions

def retrieve_user_response():
    user_options = {'R', 'P','S'}
    # prompt for user
    user_response = input("Please select R, P or S: ").upper()
    # input function returns outputs value entered by the user
    if user_response in user_options:
        return user_response
    return None

def convert_user_response(user_response):
    """
    This function uses a conditional statement to convert the letter inputted by the user
    :param user_response:
    :return: converted response
    # a docstring explains the purpose of a function
    """
    user_choice = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    return user_choice[user_response]


def retrieve_computer_response():
    return random.randint(0, 2)
    # computer generates random number between both integers

def convert_computer_response(computer_response):
    """
    This function uses a conditional statement to convert the randomised integer into a string
    :param computer_response:
    :return: converted computer response

    """
    computer_choice = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}
    return computer_choice[computer_response]


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


def play_game():
    # opening command
    welcome = "Rock,Paper or Scissors?"
    print(welcome)

    user_input = retrieve_user_response()
    converted_user_input = convert_user_response(user_input)

    computer_input = retrieve_computer_response()
    converted_computer_input = convert_computer_response(computer_input)
    
    print(f"You have selected {converted_user_input}")
    # prints the computer's choice (converted from integer)
    print(f"The computer has chosen {converted_computer_input}")
    # f string inputs the variable alongside the function inside the string
    # applies function and compares both responses to determine the winner
    winner = determine_winner(converted_user_input, converted_computer_input)
    print(winner)

if __name__ == "__main__":
    play_game()

# game logic (test code) is extracted inside main() function (in this case rock_paper_scissors)
# ensure script is only run when executed directly - can import to another program and choose to run the game
# name is a special attribute (dunda)