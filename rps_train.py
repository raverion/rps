'''rps_train'''

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
    p1_last_20_moves = ""
    p2_last_20_moves = ""
    training_data = []
    legal_moves = ["R", "P", "S"]
    n = 20

    for count in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        p1_prev_play = p1_play
        p2_prev_play = p2_play

        # Record the moves of both programs in batches of n moves.
        # This data will be used for training our bot to determine which program it is playing against
        p1_last_20_moves += str(legal_moves.index(p1_play))
        p2_last_20_moves += str(legal_moves.index(p2_play))

        # every n moves, append to the master list then start a new list
        if (count and ((count+1) % n == 0)):
            training_sample = {
                "player1_moves": p1_last_20_moves,
                "player2_moves": p2_last_20_moves,
                "player2": player2_int
            }
            training_data.append(training_sample)
            p1_last_20_moves = ""
            p2_last_20_moves = ""

    # write training_data to a JSON file
    with open(f"training_data_{player2_int}.json", "w") as outfile:
        json.dump(training_data, outfile)

    return (training_data)


# def train_model():
#     '''train_model()'''
#     df_0 = pd.read_json("training_data_0.json", dtype={
#                         'player1_moves': str, 'player2_moves': str})  # player2 = quincy
#     df_1 = pd.read_json("training_data_1.json", dtype={
#                         'player1_moves': str, 'player2_moves': str})  # player2 = abbey
#     df_2 = pd.read_json("training_data_2.json", dtype={
#                         'player1_moves': str, 'player2_moves': str})  # player2 = kris
#     df_3 = pd.read_json("training_data_3.json", dtype={
#                         'player1_moves': str, 'player2_moves': str})  # player2 = mrugesh

#     # concatenate the data from all 4 players
#     df = pd.concat([df_0, df_1, df_2, df_3], axis=0).reset_index(drop=True)

#     # split the dataframe into training and testing datasets
#     X = df[['player1_moves', 'player2_moves']]
#     y = df['player2']
#     X_train, X_test, y_train, y_test = train_test_split(
#         X, y, test_size=0.2, random_state=42)

#     # Convert the input data to numpy arrays
#     X = np.array([list(map(int, x)) for x in X])

#     # Define the number of classes
#     num_classes = len(np.unique(y))

#     # Build the neural network model
#     model = Sequential()
#     model.add(Dense(64, input_dim=40, activation='relu'))
#     model.add(Dense(32, activation='relu'))
#     model.add(Dense(num_classes, activation='softmax'))

#     # Compile the model
#     model.compile(loss='sparse_categorical_crossentropy',
#                   optimizer='adam', metrics=['accuracy'])

#     # Train the model
#     model.fit(X_train, y_train, epochs=50, batch_size=32,
#               validation_data=(X_test, y_test))

#     # Evaluate the model on the testing set
#     score = model.evaluate(X_test, y_test, verbose=0)
#     print('Test loss:', score[0])
#     print('Test accuracy:', score[1])

#     return None
