import math


# Function to calculate the Probability between 2 ratings
def Probability(r1, r2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (r1 - r2) / 400))


# Function to calculate Elo rating
# K is a constant
# d determines whether player A wins or Player B
def EloRating(Ra, Rb, K, d):

    # To calculate the Winning probability of Player B
    Pb = Probability(Ra, Rb)

    # To calculate the Winning probability of Player A
    Pa = Probability(Rb, Ra)

    # Case -1 When Player A wins updating the Elo Ratings
    if (d == 1):
        Ra = Ra + K * (1 - Pa)
        Rb = Rb + K * (0 - Pb)

    # Case -2 When Player B wins updating the Elo Ratings
    else:
        Ra = Ra + K * (0 - Pa)
        Rb = Rb + K * (1 - Pb)

    return [Ra, Rb]

# This code is contributed by
# Smitha Dinesh Semwal from Geeks for Geeks


# Takes all tournament data and runs through it calculating Elo ratings for
# each player. Since Elo is cummulative and is not decaying the only way to
# accurately calculate players' Elo is to run through each game that player
# has ever played.
def calc_comprehensive_Elo(tournament_data, player_ratings):
    for games in tournament_data:
        for i in range(len(games['games'])):
            temp_winner = games['games'][i]['winner']
            player_one = games['games'][i]['players'][0]
            player_two = games['games'][i]['players'][1]

            for each in player_ratings:
                if player_one == each.name:
                    player_one_rate = each.rating
                if player_two == each.name:
                    player_two_rate = each.rating

            if temp_winner == player_one:
                new_ratings = EloRating(player_one_rate, player_two_rate, 40, 1)
            if temp_winner == player_two:
                new_ratings = EloRating(player_two_rate, player_one_rate, 40, 1)

            for each in player_ratings:
                if (player_one == temp_winner):
                    if (player_one == each.name):
                        each.rating = new_ratings[0]
                    if (player_two == each.name):
                        each.rating = new_ratings[1]
                if (player_two == temp_winner):
                    if (player_two == each.name):
                        each.rating = new_ratings[0]
                    if (player_one == each.name):
                        each.rating = new_ratings[1]

    return player_ratings
