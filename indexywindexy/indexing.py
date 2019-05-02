#!/usr/bin/python


class IndexSearchDocuments:
    '''
    A class for indexing documents by line
    '''

    def __init__(self, doco):
        self.doco = doco
        self.filter = filter

    def indexer(self, doco):
        x = []
        y = []
        with open(doco) as file:
            for idx, val in enumerate(file.readlines()):
                print(idx, val)
                x.append(idx)
                y.append(val)
        return x

    # @staticmethod
    def idxsearch(self, doco, filter):
        with open(doco) as file:
            x = [idx for
                 idx, val in enumerate(file.readlines())
                 if any(
                  xs in val for xs in filter
                 )
                 ]
            print(x)
        return x
