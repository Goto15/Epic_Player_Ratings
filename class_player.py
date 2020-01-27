# I've got this here in case I decide to expand the amount
# of data I'm collecting.


class Player:
    def __init__(self, name, Elo=1600):
        self.name = name
        self.Elo = Elo
        # wins = 0
        # losses = 0
        # limited = 1600
        # constructed_elo = 1600

    def round_Elo(player):
        player.Elo = int(round(player.Elo))
