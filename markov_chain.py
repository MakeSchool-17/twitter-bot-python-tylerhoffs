import sys
import tokenize         # import custom tokenize class
import random


class MarkNode:
    def __init__(self):
        self.keys = {}
        self.count = 0

    def append(self, new_key):
        try:
            self.keys[new_key] += 1
        except KeyError:
            self.keys[new_key] = 1
        self.count += 1

    def freq_to_prob(self):
        for key, value in self.keys.items():
            self.keys[key] = self.keys[key] / self.count


class MarkovChain():              # class that defines the structure of the markov chain
    def __init__(self, size):
        self.table = [0] * size
        for i in range(size):
            self.table[i] = MarkNode()
        self.size = size
        self.starts = []

    def insert(self, prev_key, new_key):      # insert function that finds the has value of the key and calls the append function the appropriate linked list
        if prev_key[0] == prev_key[0].upper():
            self.starts.append(prev_key)
        hash_val = hash(prev_key)
        hash_val = hash_val % self.size
        self.table[hash_val].append(new_key)

    def walk(self):
        for node in self.table:
            node.freq_to_prob()
        start_index = random.randomint(0, len(self.starts) - 1)
        starter = self.starts[start_index]
        go = True
        final_string = starter + " "
        hash_val = hash(starter)
        hash_val = hash_val % self.size
        while go:
            prob_index = random.random()
            prob_sum = 0
            for key, value in self.table[hash_val].keys.items():
                prob_sum += value
                if prob_sum >= prob_index:
                    final_string += key + " "
                    next_word = key
                    break
            hash_val = hash(next_word)
            hash_val = hash_val % self.size


if __name__ == '__main__':
    # local_root = search_node("mystery")
    source_text = sys.argv[1]
    corpus = open(source_text, encoding='utf-8')
    entire_text = corpus.read()
    corpus.close()
    tokens = tokenize.tokenize_func(entire_text)
