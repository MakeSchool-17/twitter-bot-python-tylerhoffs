# import sys
import random
import re


def histogram(source_text):                        # function to split words from text and compile their frequencies in a dict
    my_file = open(source_text, encoding='utf-8')
    all_words = []

    entire_text = my_file.read()

    regex = re.compile("[^a-zA-Z']")                 # regex to remove all non alpha characters
    subbed = regex.sub(' ', entire_text)
    subbed = subbed.lower()
    all_words = subbed.split(' ')

    word_dict = {}

    for i in range(0, len(all_words)):          # loop to populate dict and update frequencies
        if len(all_words[i]) > 1:
            if all_words[i] in word_dict:
                word_dict[all_words[i]] = word_dict[all_words[i]] + 1
            else:
                word_dict[all_words[i]] = 1
        elif all_words[i] == "a":
            word_dict["a"] = word_dict["a"] + 1

    my_file.close()
    return word_dict


def conv_probabilities(word_dict):
    word_count = 0
    for key, value in word_dict.items():
        word_count += value

    for key, value in word_dict.items():
        word_dict[key] = value / word_count * 100

    return word_dict


def random_word(word_dict2):
    print(word_dict2)
    rand_index = random.random()
    rand_sum = 0
    for key, value in word_dict2.items():
        rand_sum += value
        if rand_sum > rand_index:
            rand_word = key
    return rand_word

if __name__ == '__main__':
    local_dict = histogram('fish.txt')
    local_dict = conv_probabilities(local_dict)
    print(random_word(local_dict))
