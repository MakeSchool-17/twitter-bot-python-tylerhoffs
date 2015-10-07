import re


def tokenize_func(text):
    text = rem_punctuation(text)
    tokens = whitespace_split(text)
    return tokens


def rem_punctuation(text):
    new_text = re.sub('[,.()]', '', text)
    return new_text


def whitespace_split(text):
    return re.split('\s+', text)
