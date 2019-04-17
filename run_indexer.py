#!/usr/bin/python
import sys
from indexing import IndexSearchDocuments

if len(sys.argv) <= 1:
    print("Please pass in the name of a document you would like to index as the first argument.")
    exit(1)

doco = sys.argv[1]
filter = sys.argv[2:]

i = IndexSearchDocuments(doco)

i.indexer(doco)
i.idxsearch(doco, filter)
