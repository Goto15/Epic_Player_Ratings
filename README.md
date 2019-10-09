# Epic Player Ratings

As of right now running the code only generates a JSON file of the resulting Elo rankings of every player who has participates in Epic Monthly tournament.

### path.json
You will need to create a path.json file within the same directory as main.py that points to the directory that holds the tournament JSON files. The path.json file should look like:

{

    "path": "directory/path/here"

}

## Elo Rating Note
Since Elo ratings don't decay, the only way to generate an Elo rating is to run through every game and adjust each players' rating accordingly.
