# import sys
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


def unique_words(word_dict):
    return len(word_dict)


def frequency(search_word, word_dict):
    return word_dict[search_word]

if __name__ == '__main__':
    local_dict = histogram('pg1661.txt')
    print('Unique words: ' + unique_words(local_dict))
    print('Frequency of "mystery": ' + frequency("mystery", local_dict))
