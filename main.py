from class_player import Player
from elo_calc import calc_comprehensive_Elo, Probability
from tourney_parser import (
    load_ordered_tournaments,
    load_all_players,
    player_ratings_to_JSON,
)

import json
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Computes ELO ratings')
parser.add_argument('-d', dest='dataDir', type=Path, metavar='DATA_DIR',
                    help='Default: whatever is in "path.json"')
parser.add_argument('-o', dest='outDir', type=Path, metavar='OUT_DIR',
                    default=Path("./Player_Ratings/"),
                    help='Generated ratings go here. Default: ./Player_Ratings/')
args = parser.parse_args()
if args.dataDir is not None:
    path = args.dataDir
else:
    # Read in the file path from the JSON file
    with open('path.json') as pathfile:
        p = json.load(pathfile)
        path = Path(p["path"])

# Create the tournament and player information lists
tournament_data = load_ordered_tournaments(path)
player_names = load_all_players(tournament_data)

# Create new ratings for each player
player_Elo_ratings = [Player(each) for each in player_names]

# Calculate and sort player Elo ratings from highest to lowest
calc_comprehensive_Elo(tournament_data, player_Elo_ratings)
player_Elo_ratings.sort(key=lambda p: -p.Elo)

# Rounds each rating to a beautiful round integer
for each in player_Elo_ratings:
    each.Elo = int(round(each.Elo))

args.outDir.mkdir(exist_ok=True)
# Creates the JSON from the player_ratings list
player_ratings_to_JSON(player_Elo_ratings, args.outDir / "Elo_ratings.json")
