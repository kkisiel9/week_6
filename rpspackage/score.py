def starting_score():
    return {"You": 0, "Computer": 0}

def updating_score(score, result):
    if result == "You win!":
        score["You"] += 1
    elif result == "You lose!":
        score["Computer"] += 1

def display_score(score):
    return f"Score - You: {score["You"]} | Computer: {score["Computer"]}"