#!/usr/bin/python


class DrunkyMunky:
    '''
    To see whether your friend is drunk or not (spoiler = they are)
    '''

    def __init__(self, drunk):
        self.drunk = drunk

    def isDrunk(drunk):
        if drunk in [1, '1']:
            stringout = 'Drunk friend is my favourite friend!'
            print(stringout)
            return stringout
        else:
            stringout = 'Please come back when your friend is drunk.'
            print(stringout)
            return stringout
