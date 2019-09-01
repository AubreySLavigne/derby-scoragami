#!/usr/bin/env python3
'''
The Team module provides functionality concerning Roller Derby Teams
'''

import csv


class Team:
    '''
    Encapsulates information about a single team
    '''
    def __init__(self, **kw):
        self.id = kw.get('id')
        self.name = kw.get('name')
        self.short_name = kw.get('short_name')
        self.abbreviation = kw.get('abbreviation')
        self.team_type = kw.get('team_type')
        self.location = kw.get('location')
        self.website = kw.get('website')
        self.parent_league = kw.get('parent_league')
        self.established_date = kw.get('established_date')
        self.disbanded_date = kw.get('disbanded_date')
        self.genus = kw.get('genus')
        self.domain = kw.get('domain')


def load_teams(filename: str = '') -> dict:
    '''
    Returns a dictionary containing all Derby teams

    The CSV is from the team data snapshot from flattrackstats.com
    '''
    res = {}

    with open(filename) as infile:
        reader = csv.reader(infile)
        for row in reader:
            # Burn the header, which contains the names of the fields
            if row[0] == 'id':
                continue

            team = Team(
                id=row[0],
                name=row[1],
                short_name=row[2],
                abbreviation=row[3],
                team_type=row[4],
                location=row[5],
                website=row[6],
                parent_league=row[7],
                established_date=row[8],
                disbanded_date=row[9],
                genus=row[10],
                domain=row[11]
            )
            res[team.id] = team

    return res
