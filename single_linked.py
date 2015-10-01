import re
import sys


class link_node():                    # class defining the structure for the node of a single linked list
        def __init__(self, key):
            self.next = None
            self.key = key
            self.freq = 1


def list_insert(root, node):          # function defining the procedure to insert a node into the list
    if root is None:
        root = node
    else:
        if root.key == node.key:    # if the key exists, increase the frequency
            root.freq += 1
        elif root.key > node.key:
            node.next = root
            root = node
        elif root.next is None:   # if the key in the node is bigger, make the node the right child if possible.
            root.next = node
        elif root.next.key > node.key:
            node.next = root.next
            root.next = node
        elif root.next.key < node.key:
            list_insert(root.next, node)
    return root


def list_print(root):
    if root is not None:
        print(root.key + ":" + str(root.freq) + " ")
        if root.next is not None:
            list_print(root.next)


def histogram(source_text):                        # function to split words from text and compile their frequencies in a linked list
    my_file = open(source_text, encoding='utf-8')
    all_words = []

    entire_text = my_file.read()

    regex = re.compile("[^a-zA-Z']")                 # regex to remove all non alpha characters
    subbed = regex.sub(' ', entire_text)
    subbed = subbed.lower()
    all_words = subbed.split(' ')

    hist_root = None

    for i in range(0, len(all_words)):          # loop to populate dict and update frequencies

        if len(all_words[i]) > 1:
            if hist_root is None:
                hist_root = link_node(all_words[i])
            else:
                new_node = link_node(all_words[i])
                print(all_words[i])
                hist_root = list_insert(hist_root, new_node)
        elif all_words[i] == "a":
            new_node = link_node(all_words[i])
            hist_root = list_insert(hist_root, new_node)
        elif all_words[i] == "i":
            new_node = link_node(all_words[i])
            hist_root = list_insert(hist_root, new_node)

    my_file.close()
    print("HISTROOT: " + hist_root.key)
    return hist_root


def frequency_search(root, word):

    if root.key == word:    # if the key exists, return the frequency
        return root.freq
    elif root.key > word:   # if the key in the node is bigger, make the node the right child if possible.
        return -1
    else:
        return frequency_search(root.next, word)  # recursive call if child exists
    return 0

if __name__ == '__main__':
    # local_root = search_node("mystery")
    source_text = sys.argv[1]
    local_root = histogram(source_text)
    list_print(local_root)
    search_frequency = frequency_search(local_root, "mystery")
    print("Frequency of 'mystery': " + str(search_frequency))
