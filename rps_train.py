import json


def generate_play_data(player1, player2, player2_int, num_games):
    '''generate_play_data()
    This will generate a JSON file from a list of dictionaries.
    Each dictionary is a training sample consisting of 2 lists as input data and an integer as a label
    The lists represent the 20 consecutive RSP moves performed by each player...
    training_sample = {"inputs": [p1_last_20_moves, p2_last_20_moves], "label": p1}
    training_data = [training_sample]
    '''

    p1_prev_play = ""
    p2_prev_play = ""

    # for recording the moves of both programs
    p1_last_20_moves = []
    p2_last_20_moves = []
    training_data = []
    legal_moves = ["R", "P", "S"]
    n = 10

    for count in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        p1_prev_play = p1_play
        p2_prev_play = p2_play

        # Record the moves of both programs in batches of n moves.
        # This data will be used for training our bot to determine which program it is playing against
        p1_last_20_moves.append(legal_moves.index(p1_play))
        p2_last_20_moves.append(legal_moves.index(p2_play))

        # every n moves, append to the master list then start a new list
        if (count and ((count+1) % n == 0)):
            training_sample = {
                "player1_moves": p1_last_20_moves,
                "player2_moves": p2_last_20_moves,
                "player2": player2_int
            }
            training_data.append(training_sample)
            p1_last_20_moves = []
            p2_last_20_moves = []

    # write training_data to a JSON file
    with open(f"training_data_{player2_int}.json", "w") as outfile:
        json.dump(training_data, outfile)

    return (training_data)
