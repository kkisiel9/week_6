# choice_display.py

#  art for Choices
display_choice = {
    "R": """🪨""",
    "P": """📄""",
    "S": """✃""",
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
    Displays the home page with a banner, ASCII art for choices, and options for the player.
    """
    # Banner for the welcome message
    banner = """
    *********************************************
                                               
        Welcome to Rock, Paper, Scissors - with  
                  a Marvel twist!             
                                               
    *********************************************
    """
    print(banner)


    # Display options
    print("\nChoose an option:")
    print("1. Start Game")
    print("2. View Leaderboard")
    print("3. Exit")

    print("\nHere are your choices:")

    # Display ASCII art for each choice
    print("\nRock (R):")
    print(display_choice["R"])

    print("\nPaper (P):")
    print(display_choice["P"])

    print("\nScissors (S):")
    print(display_choice["S"])

    print("\nThanos (T):")
    print(display_choice["T"])



