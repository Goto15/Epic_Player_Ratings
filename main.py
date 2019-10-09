from class_player import Player
from elo_calc import calc_comprehensive_Elo
from tourney_parser import (
    load_ordered_tournaments,
    load_all_players,
    player_ratings_to_JSON,
)

import json


# Lists for different player data
path = ''
player_ratings = []

# Read in the file path from the JSON file
with open('path.json') as pathfile:
    p = json.load(pathfile)
    path = p["path"]

# Create the tournament and player information lists
tournament_data = load_ordered_tournaments(path)
player_names = load_all_players(tournament_data)

# Create new ratings for each player
for each in player_names:
    player_ratings.append(Player(each))

# Calculate and sort player Elo ratings from highest to lowest
player_Elo_ratings = calc_comprehensive_Elo(tournament_data, player_ratings)
player_Elo_ratings = sorted(player_Elo_ratings, key=lambda p: -p.rating)

# Rounds each rating to a beautiful round integer
for each in player_Elo_ratings:
    each.rating = int(round(each.rating))

# Creates the JSON from the player_ratings list
player_ratings_to_JSON(player_Elo_ratings, "Elo_ratings.json")
