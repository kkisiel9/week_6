from random import randint

user_choices_meanings = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
computer_choice_meanings = {0:'Rock', 1:'Paper', 2:'Scissors'}

# user_input = input('Choose R, P or S :').upper()

# while user_input != 'R' or 'P' or 'S':
#     print('Invalid choice try again')
#     user_input = input('Choose R, P or S :').capitalize()
#     if user_input == 'R' or 'P' or 'S':
#         break





def user_conversion(key):
    return user_choices_meanings.get(key, "Invalid selection")

def computer_conversion(key):
    return  computer_choice_meanings.get(key, '')

def determining_winner(user_choice, computer_choice):
    """
    This function determines the winning combination and therefore who wins the game
    :param user_choice: takes the variable created for the user's choice
    :param computer_choice: takes the variable created for the computer's choice
    :return: returns the outcome as a string after comparing the two parameters
    """
    if user_choice == computer_choice:
        return "It's a draw"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Paper' and computer_choice == 'Rock') or (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return 'User wins'
    else:
        return 'You lose'

def main():
    while True:
        while True:
            user_input = input('Choose R, P or S :').upper()
            user_choice = user_conversion(user_input)
            print(user_choice)
            if user_choice != "":
                break
            else:
                print('Please choose a valid choice')
        computer_choice = randint(0, 2)
        computer_choice_2 = computer_conversion(computer_choice)
        print(computer_choice_2)
        winner = determining_winner(user_choice, computer_choice_2)
        print(winner)
        play_again = input('Would you like to play again Y/N')
        if play_again == 'N':
                break
if __name__ == '__main__':
    main()

