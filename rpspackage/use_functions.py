import game_functions
from rpspackage.game_functions import convert_user_response

game_functions.play_game()

user_input = game_functions.convert_user_response('R')
print(user_input)