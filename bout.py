#!/usr/bin/env python3
'''
This module contains information relating to games
'''

import csv


class Bout:
    '''
    Represents a single game that occured on the target date
    '''

    def __init__(self,
                 date='',
                 home_team='',
                 visiting_team='',
                 score=None):

        self.date = date
        self.home_team = home_team
        self.visiting_team = visiting_team
        self.score = score

    def __str__(self) -> str:

        return (f'{self.date} - {self.home_team.name} ({self.score.home})'
                f' vs {self.visiting_team.name} ({self.score.visiting})')


def next_bout(filename: str = '') -> list:
    '''
    Returns next CSV line about an individual game of Derby

    The CSV is from the bout data snapshot from flattrackstats.com
    '''
    with open(filename) as infile:
        reader = csv.reader(infile)
        for row in reader:
            if row[0] != 'id':
                yield row
