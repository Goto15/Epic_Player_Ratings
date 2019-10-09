from datetime import datetime

import json
import os


# Given a directory of JSON files
# load a chronological list of games played by all players
def load_ordered_tournaments(path):
    data = []
    files = []

    for r, d, f in os.walk(path):
        for file in f:
            if '.json' in file:
                files.append(os.path.join(r, file))

    for f in files:
        with open(f) as jsonfile:
            data.append(json.load(jsonfile))

    data = sorted(data, key=lambda data: data['info']['date'])

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

    player_list = sorted(player_list, key=lambda player_list: player_list.upper())

    return player_list


# Create the JSON file from the player ratings list
def player_ratings_to_JSON(player_ratings, file_name):
    final_ratings = {}
    final_ratings['Players'] = []

    for each in player_ratings:
        final_ratings['Players'].append({
            'name': each.name,
            'rating': each.rating
        })

    with open(file_name, 'w') as outfile:
        json.dump(final_ratings, outfile, indent=4)
