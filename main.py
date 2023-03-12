# This entrypoint file to be used in development. Start by reading README.md
# from rps_game import play, mrugesh, abbey, quincy, kris, human, random_player
from rps_game import play, quincy, kris, mrugesh, abbey
from rps import player
from rps_train import generate_play_data
# from unittest import main

# play(player, quincy, 1000)
# play(player, abbey, 1000)
# play(player, kris, 1000)
# play(player, mrugesh, 1000)

generate_play_data(player, quincy, 0, 500000)
generate_play_data(player, abbey, 1, 500000)
generate_play_data(player, kris, 2, 500000)
generate_play_data(player, mrugesh, 3, 500000)

# Uncomment line below to play interactively against a bot:
# play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)


# Uncomment line below to run unit tests automatically
# main(module='test_module', exit=False)
