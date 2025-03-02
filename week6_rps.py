import random  # Importing the random module to allow the computer to make a random choice


def convert_to_fullname(choice):
    """
    converts ('R', 'P', 'S') into the full name.
    returns None if the input is invalid.
    """
    choices_map = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    return choices_map.get(choice, None)  # uses dictionary mapping for cleaner code
    # .get() retrieves the value for the key, or returns None if key doesn't exist.


def determine_winner(player_selection, computer_choice):
    """
    Determines the winner based on the rules of Rock, Paper, Scissors.
    Returns a message indicating the result.
    """
    if player_selection == computer_choice:
        return "It's a draw!"

    winning_combinations = {
        'Rock': 'Scissors',
        'Paper': 'Rock',
        'Scissors': 'Paper'
    }
    # Check if the player's selection beats the computer's choice
    if winning_combinations[player_selection] == computer_choice:
        return "You win!"
    else:
        return "You lose!"


def get_computer_choice():
    """
    Randomly selects and returns Rock, Paper, or Scissors for the computer.
    """
    return random.choice(['Rock', 'Paper', 'Scissors'])  # More concise than using randint


def play_game():
    """
    Runs the Rock, Paper, Scissors game.
    """
    # Ask the user for input and convert it to uppercase
    user_input = input("Enter R for Rock, P for Paper, or S for Scissors: ").upper()
    player_selection = convert_to_fullname(user_input)

    if player_selection is None:
        print("Invalid choice! Please enter R, P, or S.")
        return

    computer_choice = get_computer_choice()

    print("\nYou chose:", player_selection)
    print("Computer chose:", computer_choice)

    result = determine_winner(player_selection, computer_choice)
    print(result)

# the if __name__ == "__main__": statement ensures the game runs only when the script is executed directly.
# it prevents the game from running automatically if this file is imported as a module in another script
if __name__ == "__main__":
    play_game()  # ensures the script runs only when executed directly
