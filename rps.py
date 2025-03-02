import random
import time
# importing the random module to generate integers for the computer to use as choices
# importing time to generate dramatic effect before announcing the result

user_input_to_string = {"R": "rock", "P": "paper", "S": "scissors"}
computer_options_to_letter = {0 : "R", 1: "P", 2: "S"}
# creating two dictionaries to assign keys and values
# the first one assigns the value of full string to a letter, the letters being the options a user can enter
# the second one uses computer options (0,2) and assigns values of letters to them, to match human input to it can be compared later

def convert_comp_choice(comp_choice):
    """
this function takes the integer computer generated and converts it into a letter and then a string
    :param comp_choice: integer choice (0,2). It will then be used in main to compare results
    :return: full name of computer's choice, str
    """
    # generate random in from the range above through importing the random module
    comp_choice_letter = computer_options_to_letter.get(comp_choice, "")
    # create a new variable to store obtained from the comp_choice dictionary R,P,S value
    if comp_choice_letter == "":
        return ""
    # default to pass two variables in the get method value, return "" if not found in dict
    # create a conditional
    # if "" was passed, the function would also return an empty string to handle the unexpected input
    return convert_into_string(comp_choice_letter)
# integer letter returned

def convert_into_string(choice_letter):
    # this function takes a single letter choice (user input) from the dictionary and converts it into a full name
    """
    :param choice_letter: R,P,S from the dictionary
    :return: the full name of the choice, string
    """
    return user_input_to_string.get(choice_letter, "")
 # Use the user_input_to_string dictionary to get the full name corresponding to the single-letter choice

def result(comp_choice, human_choice):
    """
    This function defines the result of the game through comparing the computer and human choice
    :param comp_choice: random int chosen by the computer from 0-3 range
    :param human_choice: input- R, P, S
    """
    if human_choice == comp_choice:
        return "tie"
    elif (human_choice == "rock" and comp_choice == "scissors") or \
            (human_choice == "scissors" and comp_choice == "paper") or \
            (human_choice == "paper" and comp_choice == "rock"):
        return "win"
    else:
        return "lose"
# multiple conditionals to compare the results and determine winner

def main():
    # main trick implemented here, with the code not forming part of any functions
    print("Welcome to the Rock, Paper, Scissors game.")
    # game starts here
    human_wins = 0
    ties = 0
    computer_wins = 0
    # scores are set to zero for score tracking purposes before we enter the loop
    # create a loop for the game to be able to run multiple times if the user wishes to
    while True:
        # the loop below checks for the user input and executes the function convert_into_string
        # it is executed through running through all the possible input choices and
        while True:
            human_choice = input("Chose R, P or S:").upper()
            # create a variable to store the human's choice
            # if passed in lowercase, it'll be converted into upper
            converted_human_choice = convert_into_string(human_choice)
            # create a variable to store the converted into a full word human choice
            # through creating a function
            #  which takes the human_choice variable collected from the human (a letter) and converts it into a full word
            if converted_human_choice != "":
                break
            #     check if the entered choice is valid, and if so break
            else:
                print("Please chose a valid value: R,P or S!")
        #         otherwise, ask the user to input again

        comp_choice = random.randrange(0, 3)
        # generate computer's choice
        converted_comp_choice = convert_comp_choice(comp_choice)
        # obtain a full name of the choice by using a function
        print(f"You chose {converted_human_choice} and the computer chose {converted_comp_choice}")
        print("Hence...")
        #
        time.sleep(1)
        # delays the result announcement in the terminal for dramatic effect

        r = result(converted_comp_choice, converted_human_choice)
        # new variable, r, to store the result obtained from the function called result
        if r == "tie":
            print("It's a tie!")
            ties += 1
        #     if r equals a tie, then the programme will print the above statement and add a point
        elif r == "win":
            print("YOU WIN!!!")
            human_wins += 1
        else:
            print("YOU LOSE!")
            computer_wins += 1
        print(f"Scores: You - {human_wins} point(s), Computer {computer_wins} point(s), Ties - {ties}")
        # printing a formatted string to present the results/scores
        question = input("Want to play again? Y/N")
        if question == "N":
            break
    # Depending on the user's input, the conditional statement breaks the loop/exits or loops agai


if __name__ == "__main__":
    main()
# implementing my main trick to ensure if someone wanted to use my functions in another file, they won't rune the body of the programme
