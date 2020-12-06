"""This is Project 4 where we will use hash tables
to implement a search engine for documents
Course: CPE 202
Quarter: Spring 2020
Author: Drew Soderquist"""

from hashtables import HashTableLinear, import_stopwords
import math
import os


def main():
    directory = input("Input the path of the directory containing documents: ")
    while os.listdir(directory) is False:
        directory = input("Directory not found. Please input the path of the directory containing documents: ")
    new_hash = HashTableLinear()
    while True:
        query = input("Input a query prepended by 's: ' to search. If you wish to quit, simply input ':q'. ")
        if query == ":q":
            return False
        words = query[3::]  # if there's a space between query and s:
        print("words", words)
        engine = SearchEngine(directory, import_stopwords("stop_words.txt", new_hash))
        results = engine.search(words)
        print_results(results)


def print_results(results):
    """prints results based on their ranking
    Args:
        results(list): list of tuples (file_name, frequency of word)
    Returns:
        N/A, only prints
    """
    print(results)


class SearchEngine:
    """Search Engine is one of
    - None, or
    - A list of tuples of files and weighted frequencies
    Attributes:
        directory(str): a directory name
        stopwords(HashMap): a hash table containing stop words
        doc_length(HashMap): a hash table containing the total number of words in each document
        term_freqs(HashMap): a hash table of hash tables for each term
    """

    def __init__(self, directory, stopwords):
        self.doc_length = HashTableLinear()
        self.term_freqs = HashTableLinear()
        self.stopwords = stopwords
        self.index_files(directory)

    def read_file(self, infile):
        """A helper function to read a file
        Args:
            infile(str): the path to a file
        Returns:
            list: a list of str read from a file
        """
        with open(infile, "r") as file:
            lines = file.read()
        # print("the lines", lines)
        lines = lines.split(" ")
        return lines  # does this return one big string???

    def parse_words(self, lines):
        """splits strings into words by spaces
        converts words to lower cases,
        and removes newline chars, parentheses, brackets such as [] and {}
        and punctuations such as , . ? ! and excludes stop words
        Args:
            lines(list): a list of strings
        Returns:
            list: a lot of words
        """
        word = ""
        punctuation = ["[", "]", "{", "}", ",", ".", "?", "!", "\n", " ", "(", ")"]
        list_of_words = []
        # lines = lines.split(" ")
        # print("lines", lines)
        for term in lines:
            #term = lines[i]
            # print("term in lines", term)
            term = term.strip()
            if "\n" in term:
                term = term.replace("\n", "")
            for letter in term:
                if letter not in punctuation:
                    if 91 > ord(letter) > 64:
                        new_letter = chr(ord(letter) + 32)
                        word += new_letter
                    else:
                        word += letter
            # i = i.split()
            # i = str(i)
            # print("this is word", word)
            list_of_words.append(word)
            word = ""
        # print("list of words", list_of_words)
        words = self.exclude_stopwords(list_of_words)
        # print("parse_words", words)
        return words

    def exclude_stopwords(self, terms):
        """excludes stopwords from the list of terms
        Args:
            terms(list): list of stop words
        Returns:
            list: a list of strings with stopwords removed
        """
        new_terms = []
        for i in terms:
            if self.stopwords.__contains__(i) is False:
                new_terms.append(i)
        return new_terms

    def count_words(self, file_path_name, words):
        """count words in a file and stores its frequency
        Args:
            file_path_name(str): the file name
            words(list): a list of words
        Returns:
            N/A
        """
        for word in words:
            new_hash = HashTableLinear()
            new_hash.put(file_path_name, 1)
            if word in self.term_freqs:  # self.term_freqs.contains(word):
                # if word in self.term_freqs is True:
                # print("HIT")
                hash_word = self.term_freqs.get(word)
                if file_path_name in self.term_freqs[word]:
                    idx = 0
                    boolean = True
                    while boolean is True:  # finds where file_path occurs
                        if hash_word.table[idx] is not None and hash_word.table[idx].key == file_path_name:
                            hash_word.table[idx].val += 1  # increments frequency by 1
                            boolean = False
                        idx += 1
                    # print("Hash word idx", hash_word.table[idx])
                    # hash_word[idx] += 1
                    # hash_word[file_path_name] += 1
                    # self.term_freqs[word][file_path_name] += 1
                else:
                    hash_word.put(file_path_name, 1)
                    # self.term_freqs[word][file_path_name] = 1
            else:
                self.term_freqs.put(word, new_hash)
        self.doc_length.put(file_path_name, len(words))
        return

    def index_files(self, directory):
        """index all text files in a given directory
        Args:
            directory(str): the path of a directory
        Returns:
            N/A
        """
        # print("index files")
        list_dir = os.listdir(directory)
        # print("list_dir", list_dir)
        for i in list_dir:
            print(i)
            path = os.path.join(directory, i)
            if os.path.isfile(path) is True:
                # print("hit")
                parts = os.path.splitext(i)
                if parts[1] == ".txt":
                    # print("called count")
                    read = self.read_file(path)
                    words = self.parse_words(read)
                    # print("parse", words, "file", directory)
                    self.count_words(i, words)
        # pass  # spec sheet kinda confusing

    def get_wf(self, tf):
        """computes the weighted frequency
        Args:
            tf(float): term frequency
        Returns:
            float: the weighted frequency
        """
        if tf > 0:
            wf = 1 + math.log(tf)
        else:
            wf = 0
        return wf

    def get_scores(self, terms):
        """creates a list of scores for each file in corpus
        Args:
            terms(list): a list of str
        Returns:
            list: a list of Tuples, each containing the file_path_name and it relevancy score
        """
        print("terms", terms)
        scores = HashTableLinear()
        for i in terms:
            try:
                hash_files = self.term_freqs.get(i)
                print("hash", hash_files)
                for j in range(hash_files.table_size):
                    if hash_files.table[j] is not None:
                        freq = hash_files.table[j].val  # j.table.val  # hash_tab.get(j)
                        wf_score = self.get_wf(freq)
                        # actual_freq = freq + wf_score
                        scores.put(hash_files.table[j].key, 0)
                        scores[hash_files.table[j].key] = wf_score + self.get_wf(hash_files.table[j].val)  # actual_freq
            except KeyError:
                print("files does not contain")
        list_scores = []
        for k in range(scores.table_size):
            if scores.table[k] is not None:
                scores.table[k].val /= self.doc_length.get(scores.table[k].key)
                # scores.table[k].val /= self.doc_length[scores.table[k].key]
                list_scores.append((scores.table[k].key, scores.table[k].val))
        return list_scores

    def rank(self, scores):
        """ranks the files in the descending order of relevancy
        Args:
            scores(list): a list of tuples -> (file_path_name, score)
        Returns:
            list: a list of tuples (file_path_name, score) sorted in descending order of relevancy
        """
        sorted_scores = scores
        for i in range(len(sorted_scores) - 1):  # for n passes
            for k in range(len(sorted_scores) - 1):  # for n comparisons
                if sorted_scores[k][1] < sorted_scores[k + 1][1]:
                    val1 = sorted_scores[k]
                    sorted_scores[k] = sorted_scores[k + 1]
                    sorted_scores[k + 1] = val1
        return sorted_scores

    def search(self, query):
        """search for the query terms in files
        Args:
            query(str): query input, ex: 'computer science'
        Returns:
            list: a list of tuples (file_path_name, score) sorted in descending order of relevancy
        """
        query = query.split(" ")
        words = self.parse_words(query)  # maybe just pass in query
        # print("this is words", words)
        scores = self.get_scores(words)
        sorted_scores = self.rank(scores)
        return sorted_scores


if __name__ == '__main__':
    main()

