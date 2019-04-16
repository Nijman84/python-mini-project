#!/usr/bin/python
import unittest
# from indexing import IndexSearchDocuments


class TestIndexerDocuments(unittest.TestCase):

    def testIndexer(self):
        self.assertEqual(2, 2)

    def testSearcher(self):
        self.assertTrue(1 == 1)

    def testFalse(self):
        self.assertFalse(1 != 1)


if __name__ == "__main__":
    unittest.main()
