#!/usr/bin/python
import sys

if len(sys.argv) <= 1:
    print("Please pass in the name of a document you would like to index as the first argument.")
    exit(1)

doco = sys.argv[1]
filter = sys.argv[2:]


class IndexSearchDocuments:
    '''
    A class for indexing documents by line
    '''

    def __init__(self, doco):
        self.doco = doco

    def indexer(doco):
        with open(doco) as file:
            for idx, val in enumerate(file.readlines()):
                print(idx, val)

    def idxsearch(doco, filter):
        with open(doco) as file:
            x = [idx for
                 idx, val in enumerate(file.readlines())
                 if any(
                  xs in val for xs in filter
                 )
                 ]
            print(x)
        return x


IndexSearchDocuments.indexer(doco)
IndexSearchDocuments.idxsearch(doco, filter)
