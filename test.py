#!/usr/bin/python
import unittest
from indexing import IndexSearchDocuments

doco = 'sampledoc.md'

i = IndexSearchDocuments(doco)


class TestIndexerDocuments(unittest.TestCase):

    def test1(self):
        filter = ['is']
        result = i.idxsearch(doco, filter)
        self.assertEqual(result, [0, 1, 4, 5])

    def test2(self):
        filter = ['is', 'Another']
        result = i.idxsearch(doco, filter)
        self.assertEqual(result, [0, 1, 2, 4, 5])

    def test3(self):
        filter = ['bored', 'OMG', 'Here']
        result = i.idxsearch(doco, filter)
        self.assertEqual(result, [1, 3, 5])

    def test4(self):
        result = i.indexer(doco)
        print(result)
        print(len(result))
        self.assertTrue(len(result) == 6)


if __name__ == "__main__":
    unittest.main()
