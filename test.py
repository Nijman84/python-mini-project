#!/usr/bin/python
import unittest
from indexywindexy.indexing import IndexSearchDocuments
from drunkenwunken.drunken import DrunkyMunky

doco = 'indexywindexy/sampledoc.md'

i = IndexSearchDocuments(doco)
# d = DrunkyMunky.isDrunk


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

    def test_drunken_drunk(self):
        drunk = 1
        result = DrunkyMunky.isDrunk(drunk)
        self.assertEqual(result, 'Drunk friend is my favourite friend!')

    def test_drunken_drunkstr(self):
        drunk = '1'
        result = DrunkyMunky.isDrunk(drunk)
        self.assertEqual(result, 'Drunk friend is my favourite friend!')

    def test_drunken_not_drunk(self):
        drunk = 0
        result = DrunkyMunky.isDrunk(drunk)
        self.assertEqual(result, 'Please come back when your friend is drunk.')

    def test_drunken_not_drunk_str(self):
        drunk = 'this is a string'
        result = DrunkyMunky.isDrunk(drunk)
        self.assertEqual(result, 'Please come back when your friend is drunk.')

    def test_drunken_not_drunk_emptystring(self):
        drunk = ''
        result = DrunkyMunky.isDrunk(drunk)
        self.assertEqual(result, 'Please come back when your friend is drunk.')

    def test_drunken_not_drunk_null(self):
        drunk = None
        result = DrunkyMunky.isDrunk(drunk)
        self.assertEqual(result, 'Please come back when your friend is drunk.')


if __name__ == "__main__":
    unittest.main()
