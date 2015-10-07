# [a-zA-Z]+-?\.?,?\!?\??
import re
import sys


def parse_text(source_text):                        # function to split words from text and compile their frequencies in a linked list
    my_file = open(source_text, encoding='utf-8')

    entire_text = my_file.read()

    regex = re.compile("[^a-zA-Z\ \!\?,\.\-:&()\n'\";]")      # regex to remove all non alpha characters
    subbed = regex.sub('', entire_text)

    my_file.close()
    return subbed

if __name__ == '__main__':
    # local_root = search_node("mystery")
    source_text = sys.argv[1]
    new_text = parse_text(source_text)
    my_file = open(source_text, 'w')
    my_file.write(new_text)
    my_file.close()
