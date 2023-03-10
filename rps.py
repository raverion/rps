# The example function below keeps track of the opponent's history and
# plays whatever the opponent played two plays ago. It is not a very good player
# so you will need to change the code to pass the challenge.
'''RPS module'''


def player(prev_play, opponent_history=[]):
    '''player function'''
    opponent_history.append(prev_play)

    # if len(opponent_history) > 2:
    #     guess = opponent_history[-2]
    guess = "S"
    if prev_play == "R":
        guess = "P"
    elif prev_play == "S":
        guess = "R"
    else:
        guess = "S"

    return guess
