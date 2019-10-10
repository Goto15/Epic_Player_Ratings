from .. import elo_calc

import pytest


# Probability should return the chance that r1 loses to r2
@pytest.mark.parametrize("r1, r2, expected", [
                        (1700, 1510, .25),
                        (1600, 1600, .5),
                        (2400, 0,    0),
                        (0,    2400, 1),
                        (-100, 5000, 1),
                        (5000, -100, 0)])
def test_Probability(r1, r2, expected):
    assert round(elo_calc.Probability(r1, r2), 2) == expected


# EloRating should return the adjusted Elo rates when r1 beats r2
@pytest.mark.parametrize("r1,  r2,   k,  new_r1, new_r2", [
                        (1600, 1600, 40, 1620,   1580),
                        (1700, 1510, 40, 1710,   1500),
                        (1510, 1700, 40, 1540,   1670),
                        (0,    2400, 40, 40,     2360),
                        (2400, 0,    40, 2400,   0)])
def test_EloRating(r1, r2, k, new_r1, new_r2):
    assert elo_calc.EloRating(r1, r2, k) == [new_r1, new_r2]
