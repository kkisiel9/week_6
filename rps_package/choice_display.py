# choice_display.py

# ASCII art for Choices
display_choice = {
    "R": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____) """,
    "P": """
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    """,
    "S": """
        _______
    ---'   ____)____
              ______)
          (____)
    ---.__(___)
    """,
    "T": """
        *********
    ---'   *****)____
              ******)
              *******)
    ---.**********)
    """
}

def display_home_page():
    """
    Displays the home page with art for choices and options for the player.
    """
    print("Welcome to Rock, Paper, Scissors - with a Marvel twist!")
    # Display options
    print("\nChoose an option:")
    print("1. Start Game")
    print("2. View Leaderboard")
    print("3. Exit")

    print("\nHere are your choices:")
    # Display art for each choice
    print("\nRock (R):")
    print(display_choice["R"])

    print("\nPaper (P):")
    print(display_choice["P"])

    print("\nScissors (S):")
    print(display_choice["S"])

    print("\nThanos (T):")
    print(display_choice["T"])

