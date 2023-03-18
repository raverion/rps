'''rps_game module'''
import pandas as pd
from joblib import load


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
