from datetime import datetime

import json
import os


# Given a directory of JSON files
# load a chronological list of games played by all players
def load_ordered_tournaments(path):
    files = path.glob("*.json")
    data = [json.loads(f.read_text()) for f in files]
    data.sort(key=lambda item: item['info']['date'])
    return data


# Given a list of tournament games return a list of all players
def load_all_players(tournament_list):
    player_list = []

    for games in tournament_list:
        for each in range(len(games['games'])):
            if games['games'][each]['players'][0] not in player_list:
                player_list.append(games['games'][each]['players'][0])
            if games['games'][each]['players'][1] not in player_list:
                player_list.append(games['games'][each]['players'][1])

    player_list.sort(key=lambda item: item.upper())

    return player_list


# Create the JSON file from the player ratings list
def player_ratings_to_JSON(player_ratings, path):
    final_ratings = {
        'Players': [
            {
                'name': each.name,
                'rating': each.rating
            }
            for each in player_ratings
        ]
    }

    with open(path, 'w') as outfile:
        json.dump(final_ratings, outfile, indent=4)
