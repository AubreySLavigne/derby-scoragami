#!/usr/bin/env python3
'''
This module details the results of a given match
'''

class Score:
    '''
    The result of a single game
    '''

    def __init__(self, home, visiting):
        self.home = int(home)
        self.visiting = int(visiting)

    def __eq__(self, other) -> bool:
        '''
        Two scores are equal if their winning and losing scores match,
        regardless of their order.

        This means that the score 15-23 is equivalent to 23-15
        '''
        return self.winning() == other.winning() \
            and self.losing() == other.losing()

    def __hash__(self) -> int:
        '''
        Returns a unique hash for this score
        '''
        return self.winning() * 10000 + self.losing()

    def losing(self) -> int:
        '''
        Returns the losing score of the pair, whichever is lower
        '''
        return self.home if self.home < self.visiting else self.visiting

    def winning(self) -> int:
        '''
        Returns the winning score of the pair, whichever is higher
        '''
        return self.home if self.home > self.visiting else self.visiting
