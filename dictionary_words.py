import random
import sys


def get_words():
    my_file = open('/usr/share/dict/words', encoding='utf-8')
    all_words = []
    num_words = sys.argv[1]
    new_set = []

    with open('/usr/share/dict/words', encoding='utf-8') as my_file:
        for line in my_file:
            all_words.append(line[:len(line)-1])

    while len(new_set) < int(num_words):
        rand_index = random.randint(0, len(all_words) - 1)
        new_set.append(all_words[rand_index])

    my_file.close()
    return new_set

if __name__ == '__main__':
    words = get_words()
    print(' '.join(words))
