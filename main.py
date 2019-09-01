#!/usr/bin/env python3
'''
This script identifies Scoragami within the history of Roller Derby.

Each scoragami is output when it is found (the snapshot file is ordered by
ascending time), and the final result is loaded as an image
'''

import sys

import numpy as np
from PIL import Image

from bout import Bout, next_bout
from score import Score
from team import load_teams

IMPOSSIBLE = [0, 0, 0]
AVAILABLE = [255, 255, 255]
LIGHT_RULER = [200, 200, 200]
DARK_RULER = [100, 100, 100]
FOUND = [255, 0, 255]

def main():

    img = ScoragamImage(max_score=400)

    previous_scores = {}

    scoragami_count = 0
    non_scoragami_count = 0

    teams = load_teams(filename='data/sample_teams.csv')

    for data in next_bout('data/sample_bouts.csv'):

        try:
            home_team = teams[data[4]]
            visiting_team = teams[data[6]]
            score = Score(home=data[5], visiting=data[7])
        except ValueError:
            continue
        except KeyError:
            continue

        bout = Bout(
            date=data[1],
            home_team=home_team,
            visiting_team=visiting_team,
            score=score
        )

        if hash(bout.score) not in previous_scores:
            print(f'SCORAGAMI: {bout}')
            scoragami_count += 1
            img.mark(bout.score)

            previous_scores[hash(bout.score)] = True
        else:
            non_scoragami_count += 1

    print(f'# of Scoragamis: {scoragami_count}')
    print(f'# of Others    : {non_scoragami_count}')

    img.show()


class ScoragamImage:
    '''
    Formats the resulting scoragamis as an image
    '''
    def __init__(self, max_score: int = 999):
        self.max_score = max_score
        self.pixels = np.zeros((self.max_score+1, self.max_score+1, 3), dtype=np.uint8)

        self.fill_initial()


    def fill_initial(self) -> None:
        '''
        Initialize the grid with their initial values

        Impossible scores (e.g. a winner with a lower score than a loser) are marked black

        Possible Scores are marked white
        '''
        for row in range(self.max_score):
            for col in range(self.max_score):
                if row % 100 == 0 or col % 100 == 0:
                    self.pixels[col, row] = DARK_RULER if row < col else LIGHT_RULER
                else:
                    self.pixels[col, row] = IMPOSSIBLE if row < col else AVAILABLE

    def show(self) -> None:
        '''
        Display the generated image
        '''
        img = Image.fromarray(self.pixels)
        img.show()

    def mark(self, score: Score) -> None:
        '''
        Mark the pixel for the target score
        '''
        losing = score.losing() if score.losing() < self.max_score else self.max_score
        winning = score.winning() if score.winning() < self.max_score else self.max_score
        self.pixels[losing, winning] = FOUND


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as err:
        print(err)
        sys.exit(1)
