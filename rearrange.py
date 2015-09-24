import random
import sys


def re_arrange_words():
    word_set = sys.argv[1:]
    new_set = []
    while len(word_set) > 0:
        rand_index = random.randint(0, len(word_set) - 1)
        new_set.append(word_set.pop(rand_index))
    return new_set

if __name__ == '__main__':
    words = re_arrange_words()
    print(' '.join(words))
