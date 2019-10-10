from .. import elo_calc

import pytest


# Probability should return the chance that player 1 loses to player 2
def test_Probability():
    assert round(elo_calc.Probability(1700, 1509), 3) == .25
