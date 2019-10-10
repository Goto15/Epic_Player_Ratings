import math


# Calculates the Probability between 2 ratings
def Probability(r1, r2):
    return 1 / (1 + math.pow(10, (r1 - r2) / 400))


# Function to calculate Elo rating
# when player A wins against player B
# K is a constant
def EloRating(Ra, Rb, K):

    # To calculate the Winning probability of Player B
    Pb = Probability(Ra, Rb)

    # To calculate the Winning probability of Player A
    Pa = Probability(Rb, Ra)

    # Calculate new ratings and then round them
    # One side effect of this is that players >1600 could round up one point
    # and players <1600 could be rounded down 1 point. Will need to revisit
    # in the future.
    Ra += round(K * (1 - Pa))
    Rb += round(K * (0 - Pb))

    return [Ra, Rb]

# This code is contributed by
# Smitha Dinesh Semwal from Geeks for Geeks


# Takes all tournament data and runs through it calculating Elo ratings for
# each player. Since Elo is cummulative and is not decaying the only way to
# accurately calculate players' Elo is to run through each game that player
# has ever played.
def calc_comprehensive_Elo(tournament_data, player_ratings):
    for games in tournament_data:
        for game in games['games']:
            temp_winner = game['winner']
            assert temp_winner in game['players'] and len(game['players']) == 2
            temp_loser = next(filter(lambda x: x != temp_winner, game['players']))

            for each in player_ratings:
                if temp_winner == each.name:
                    winner = each
                if temp_loser == each.name:
                    loser = each

            new_ratings = EloRating(winner.Elo, loser.Elo, 40)
            winner.Elo = new_ratings[0]
            loser.Elo = new_ratings[1]
