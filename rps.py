import random
import time
# importing the random module to generate integers for the computer to use as choices
# importing time to generate dramatic effect before announcing the result

user_to_string_convertion = {"R": "Rock", "P": "Paper", "S": "Scissors"}
computer_options = {0 : "R", 1: "P", 2: "S"}
# creating two dictionaries to assign keys and values
#

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

def convert_into_string(key):
    # this function takes
    """
    :param human_choice:
    :return:
    """
    return user_to_string_convertion.get(key, "")

def convert_comp_choice(comp_choice):
    """

    :param comp_choice:
    :return:
    """
    # generate random in from the range above through importing the random module
    # conversion of the computer choice/random integer into a string which corresponds to r/p/s
    key = computer_options.get(comp_choice, "")
    if key == "":
        return ""
    return convert_into_string(key)
#

def main():
    # main trick implemented here, with the code not forming part of any functions
    print("Welcome to the Rock, Paper, Scissors game.")
    # game starts here
    human_wins = 0
    ties = 0
    computer_wins = 0
    # scores are zero'd for score tracking purposes before we enter the loop
    # create a loop for the game to be able to run multiple times if the user wishes to
    while True:
        # the loop below checks for the user input and executes the function convert_into_string
        # it is executed through running through all the possible input choices and
        while True:
            human_choice = input("Chose R, P or S:").upper()
            # create a variable to store the human's choice
            # if passed in lowercase, it'll be converted into upper
            converted_human_choice = convert_into_string(human_choice)
            # this function takes the human_choice variable collected from the human
            # it then
            if converted_human_choice != "":
                break
            else:
                print("Please chose a valid value: R,P or S!")

        comp_choice = random.randrange(0, 3)
        converted_comp_choice = convert_comp_choice(comp_choice)
        print(f"You chose {converted_human_choice} and the computer chose {converted_comp_choice}")
        print("Hence...")
        #
        time.sleep(1)
        # delays the result announcement in the terminal

        r = result(converted_comp_choice, converted_human_choice)
        if r == "tie":
            print("It's a tie!")
            ties += 1
        elif r == "win":
            print("YOU WIN!!!")
            human_wins += 1
        else:
            print("YOU LOSE!")
            computer_wins += 1
        # depending on what the result is, a point is added to the score
        print(f"Scores: You - {human_wins} point(s), Computer {computer_wins}, Ties - {ties}")
        question = input("Want to play again? Y/N")
        if question == "N":
            break
    # Depending on the user's input, the conditional statement breaks the loop/exits or loops agai


if __name__ == "__main__":
    main()
# implementing my main trick to ensure if someone wanted to use my functions in another file, they won't rune the body of the programme
