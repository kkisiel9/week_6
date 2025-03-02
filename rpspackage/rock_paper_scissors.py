from rpspackage.game_functions import *
# importing all functions
import score

def play_game():

    game_score = score.starting_score()
    # variable = beginning score function

    welcome = "Rock,Paper or Scissors?"
    border = "#" * (len(welcome))
    print(border)
    print(welcome)
    print (border)
    # opening command

    while True:
        user_input = retrieve_user_response()
        if user_input is None:
            print("Invalid choice. Game over!")
            break
        # variable - get user response
        # if return is none the loop breaks and starts over until the user inputs a valid response

        converted_user_input = convert_user_response(user_input)
        # variable - converted user response
        computer_input = retrieve_computer_response()
        # randomised computer input
        converted_computer_input = convert_computer_response(computer_input)
        # converted computer input

        print(f"You have selected {converted_user_input}")
        print(f"The computer has chosen {converted_computer_input}")
        # f string inputs the variable alongside the function inside the string

        winner = determine_winner(converted_user_input, converted_computer_input)
        print(winner)
        # applies function and compares both responses to determine the winner


        score.updating_score(game_score, determine_winner(converted_user_input,converted_computer_input))
        # game score (original) and function to compare both score
        # function (updating_score) adds 1 to either team

        score.display_score(game_score)
        print(score.display_score(game_score))
        # displays dictionary of scores for each side

        while True:
        # Ensure valid input for play_again - set a variable
            user_replay = play_again()
            if user_replay is None:
                print("Invalid response. Please enter 'Y' for Yes or 'N' for No.")
            # condition if input is invalid
            else:
                break
        #  correct answer - loop breaks

        if not user_replay:
            #  if play again is false (No)
            print("Thank you for playing! The final score is:")
            print(score.display_score(game_score))
            break
        # exit loop and game ends


if __name__ == "__main__":
    play_game()
    # game logic (test code) is extracted inside main() function (in this case rock_paper_scissors)
    # ensure script is only run when executed directly - can import to another program and choose to run the game
    # name is a special attribute (dunda)