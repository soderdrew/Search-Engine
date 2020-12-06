"""This is Project 4 where we will use hash tables
to implement a search engine for documents
Course: CPE 202
Quarter: Spring 2020
Author: Drew Soderquist"""

from project4 import main, SearchEngine
from hashtables import import_stopwords, HashTableLinear
import unittest


class MyTestCase(unittest.TestCase):
    def test_search(self):
        new_hash = HashTableLinear()
        stopwords = import_stopwords("stop_words.txt", new_hash)
        engine = SearchEngine("docs", stopwords)
        lines = engine.read_file("test.txt")
        self.assertEqual(lines[0], "computer")
        # print(lines)
        word = engine.exclude_stopwords(lines)
        self.assertEqual(word[0], "computer")
        words = engine.parse_words(lines)
        self.assertEqual(words[1], "science")
        engine.count_words("test.txt", words)
        scores = engine.get_scores(words)
        # print("scores", scores)
        sorted = engine.search("science")
        self.assertEqual(sorted[1][0], "information_retrieval.txt")
        # print(engine.get_wf())
        # print(engine.get_wf(1))


        #print(engine.read_file("proj4.txt"))

        # parse, getscore, getwf, rank


if __name__ == '__main__':
    unittest.main()
