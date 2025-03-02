from rpspackage.game_functions import *
import score

def play_game():
    # opening command
    game_score = score.starting_score()
    welcome = "Rock,Paper or Scissors?"
    print(welcome)

    while True:
        user_input = retrieve_user_response()
        if user_input is None:
            print("Invalid choice. Game over!")
            break
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

        score.updating_score(game_score,determine_winner(converted_user_input,converted_computer_input))
        score.display_score(game_score)
        print(score.display_score(game_score))

        if not play_again():
            print("Thank you for playing! The final score is:")
            print(score.display_score(game_score))
            break

if __name__ == "__main__":
    play_game()