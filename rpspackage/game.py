import random
# import module: random variable generator

# created three functions
def user_conversion(user_response):
    """
    This function uses a conditional statement to convert the letter inputted by the user
    :param user_response:
    :return: converted response
    # a docstring explains the purpose of a function
    """
    if user_response == "R":
        return "Rock"
    elif user_response == "P":
        return "Paper"
    elif user_response == "S":
        return "Scissors"
    else:
        return "Invalid answer"
# double equality operators - is the user response equal to the string?
# function has a parameter, making it more reusable
# if statement is used for conditional execution - if initial condition is not true, the program will check the other conditions (elif, else)

def computer_conversion(computer_choice):
    """
    This function uses a conditional statement to convert the randomised integer into a string
    :param computer_choice:
    :return: converted computer response

    """
    if computer_choice == 0:
        return "Rock"
    elif computer_choice == 1:
        return "Paper"
    else:
        return "Scissors"
# computer_choice will output an integer
# return a string

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
    if outcomes[user_response] == computer_choice:
        return "You win!"
    # [] looks up the key in the dictionary, if the value is = to the computer's choice, the user wins
    # if the key does not match up to the computer's choice, the user loses
    else:
        return "You lose!"


def rock_paper_scissors():
    # opening command
    welcome = "Rock,Paper or Scissors?"
    print(welcome)
    # prompt for user
    user_response = input("Please select R, P or S: ").upper()
    # input function returns outputs value entered by the user
    print(f"You have selected {user_conversion(user_response)}")
    # computer generates random number between both integers
    computer_choice = random.randint(0, 2)
    # returns a random integer between a and b
    # prints the computer's choice (converted from integer)
    print(f"The computer has chosen {computer_conversion(computer_choice)}")
    # f string inputs the variable alongside the function inside the string
    # applies function and compares both responses to determine the winner
    winner = determine_winner(user_conversion(user_response), computer_conversion(computer_choice))
    print(winner)

rock_paper_scissors()

# THE MAIN TRICK
if __name__ == "__rock_paper_scissors__":
    rock_paper_scissors()

# game logic (test code) is extracted inside main() function (in this case rock_paper_scissors)
# ensure script is only run when executed directly - can import to another program and choose to run the game
# name is a special attribute (dunda)