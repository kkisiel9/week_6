import random
import time
from choice_display import display_choice
# Special Moves
SPECIAL_MOVES = {
    "T": "Thanos"  # Thanos evaporates everything but can only be used once per game
}

def convert_choice(choice):
    """
    Converts shorthand choices (R, P, S, T) to their full names.
    :param choice: The shorthand choice (R, P, S, T).
    :return: The full name of the choice.
    """
    choice_dict = {
        "R": "Rock",
        "P": "Paper",
        "S": "Scissors",
        "T": "Thanos"
    }
    return choice_dict.get(choice, "Invalid Choice")

def number_of_players():
    """
    Prompts the user to choose the number of players (1 or 2).
    :return: The number of players as an integer.
    """
    while True:
        user_player_option = input("Enter 1 for 1 player, 2 for 2 Players: ")
        if user_player_option in ["1", "2"]:
            return int(user_player_option)
        else:
            print("Invalid input. Please enter 1 or 2.")

def player_choice(player_name, special_move_available):
    """
    Prompts the player to enter their choice (R, P, S, or T if available).
    :param player_name: The name of the player.
    :param special_move_available: Whether the special move (Thanos) is available.
    :return: The player's choice.
    """
    while True:
        choice = input(f"{player_name}, enter R for Rock, P for Paper, S for Scissors, or T for Thanos (if available): ").upper()
        if choice in ['R', 'P', 'S']:
            return choice
        elif choice == 'T' and special_move_available:
            return choice
        else:
            print("Invalid input. Please enter R, P, S, or T (if available).")

def computer_choice():
    """
    Generates a random choice for the computer.
    :return: The computer's choice (R, P, or S).
    """
    choices = ["R", "P", "S"]
    return random.choice(choices)

def determine_winner(player1_choice, player2_choice, player2_name="Computer"):
    """
    Determines the winner of a round based on the players' choices.
    :param player1_choice: Player 1's choice.
    :param player2_choice: Player 2's choice.
    :param player2_name: The name of Player 2 (default is "Computer").
    :return: A string indicating the result of the round.
    """
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == 'R' and player2_choice == 'S') or \
         (player1_choice == 'P' and player2_choice == 'R') or \
         (player1_choice == 'S' and player2_choice == 'P') or \
         (player1_choice == 'T'):  # Thanos beats everything
        return "Player 1 wins!"
    else:
        return f"{player2_name} wins!"

def display_users_choice(choice):
    """
    Displays users choice for the chosen move.
    :param choice: The player's choice (R, P, S, or T).
    """
    if choice in display_choice:
        print(display_choice[choice])
    elif choice == 'T':
        print("\n Thanos! Everything evaporates! \n")

def play_round(num_players, player1_score, player2_score, player1_special_move_available, player2_special_move_available):
    """
    Plays a single round of the game.
    :param num_players: The number of players (1 or 2).
    :param player1_score: Player 1's current score.
    :param player2_score: Player 2's current score.
    :param player1_special_move_available: Whether Player 1 can use the special move.
    :param player2_special_move_available: Whether Player 2 can use the special move.
    :return: Updated scores and special move availability.
    """
    print("\n" + "*" * 30)
    player1_choice = player_choice("Player 1", player1_special_move_available)
    if player1_choice == 'T':
        player1_special_move_available = False

    if num_players == 1:
        player2_choice = computer_choice()
        player2_name = "Computer"
    else:
        player2_choice = player_choice("Player 2", player2_special_move_available)
        if player2_choice == 'T':
            player2_special_move_available = False
        player2_name = "Player 2"

    print(f"\nPlayer 1 chose: {convert_choice(player1_choice)}")
    display_users_choice(player1_choice)
    time.sleep(2)  # Added for dramatic effect

    print(f"{player2_name} chose: {convert_choice(player2_choice)}")
    display_users_choice(player2_choice)
    time.sleep(2)

    result = determine_winner(player1_choice, player2_choice, player2_name)
    print("\n" + result + "\n")

    if "Player 1" in result:
        player1_score += 1
    elif player2_name in result:
        player2_score += 1

    print(f"Score - Player 1: {player1_score}, {player2_name}: {player2_score}")
    return player1_score, player2_score, player1_special_move_available, player2_special_move_available

def play_game():
    """
    Manages the game flow, including initialising scores and  multiple rounds.
    """
    print("\nWelcome to Rock, Paper, Scissors - with a Marvel twist!")
    num_players = number_of_players()

    player1_score = 0
    player2_score = 0
    player1_special_move_available = True
    player2_special_move_available = True
    rounds_played = 0

    # Best of 3 logic
    while player1_score < 2 and player2_score < 2:
        rounds_played += 1
        print(f"\nRound {rounds_played}!")
        player1_score, player2_score, player1_special_move_available, player2_special_move_available = play_round(
            num_players, player1_score, player2_score, player1_special_move_available, player2_special_move_available
        )

    # Determine the overall winner
    if player1_score > player2_score:
        print("\n Player 1 wins the game!")
    else:
        print(f"\n {num_players == 1 and 'Computer' or 'Player 2'} wins the game!")

    print("\nThanks for playing! Final Scores:")
    print(f"Player 1: {player1_score}, {num_players == 1 and 'Computer' or 'Player 2'}: {player2_score}")


def main():
    # Test player_choice function
    print("Testing player_choice function...")
    test_choice = player_choice("Player 1", special_move_available=True)
    print(f"Player 1 chose: {test_choice}")

    # Initialise variables for play_round
    num_players = 1  # 1 player (vs computer)
    player1_score = 0
    player2_score = 0
    player1_special_move_available = True
    player2_special_move_available = True

    # Test play_round function
    print("\nTesting play_round function...")
    player1_score, player2_score, player1_special_move_available, player2_special_move_available = play_round(
        num_players, player1_score, player2_score, player1_special_move_available, player2_special_move_available
    )

    # Print results
    print(f"\nUpdated Scores - Player 1: {player1_score}, Computer: {player2_score}")
    print(f"Player 1 special move available: {player1_special_move_available}")
    print(f"Player 2 special move available: {player2_special_move_available}")

# Run the main function
if __name__ == "__main__":
    play_game()
    # you can use the main() to test just the def test function
    # main()

