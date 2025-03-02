def starting_score():
    """
    This function uses a dictionary to set the starting score values for the user and computer.
    The keys are the user and the computer, the values are both set to 0
    :return: dictionary with initial scores
    """
    return {"You": 0, "Computer": 0}
# returns the starting value

def updating_score(score, result):
    """
    This function updates the score dictionary based on the results.
    :param score: dictionary containing current scores
    :param result: string indicating outcome
    :return: None - function modifies set score dictionary
    """
    if result == "You win!":
        score["You"] += 1
    elif result == "You lose!":
        score["Computer"] += 1
# conditional statement based on scores - adds one to score value

def display_score(score):
    """
    This function returns a formatted string displaying the current score.
    :param score: dictionary
    :return: formatted string
    """
    return f"Score - You: {score["You"]} | Computer: {score["Computer"]}"
# string - score - key and value