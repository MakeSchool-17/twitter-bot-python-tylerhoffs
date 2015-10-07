import re
import sys


class search_node():                    # class defining the structure for the node of a binary search tree
        def __init__(self, key):
            self.l_child = None
            self.r_child = None
            self.key = key
            self.freq = 1


def tree_insert(root, node):          # function defining the procedure to insert a node into the tree
    if root is None:
        # print(root.key)
        print(node.key)
        root = node

    else:
        if root.key == node.key:    # if the key exists, increase the frequency
            root.freq += 1
        elif root.key < node.key:   # if the key in the node is bigger, make the node the right child if possible.
            if root.r_child is None:
                root.r_child = node
            else:
                tree_insert(root.r_child, node)     # recursive call if child exists
        elif root.key > node.key:   # if the key in the node is smaller, make the node the left child if possible.
            if root.l_child is None:
                root.l_child = node
            else:
                tree_insert(root.l_child, node)     # recursive call if child exists


def tree_print(root):
    if root is not None:
        print(root.key + " " + str(root.freq))
        if root.l_child is not None:
            tree_print(root.l_child)
        if root.r_child is not None:
            tree_print(root.r_child)


def histogram(source_text):                        # function to split words from text and compile their frequencies in a dict
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
                hist_root = search_node(all_words[i])
            else:
                new_node = search_node(all_words[i])
                tree_insert(hist_root, new_node)
        elif all_words[i] == "a":
            new_node = search_node(all_words[i])
            tree_insert(hist_root, new_node)
        elif all_words[i] == "i":
            new_node = search_node(all_words[i])
            tree_insert(hist_root, new_node)

    my_file.close()
    return hist_root


def frequency_search(root, word):

    if root.key == word:    # if the key exists, return the frequency
        return root.freq
    elif root.key < word:   # if the key in the node is bigger, check the right child if possible.
        if root.r_child is None:
            return -1
        else:
            return frequency_search(root.r_child, word)     # recursive call if child exists
    elif root.key > word:   # if the key in the node is smaller, check the left child if possible.
        if root.l_child is None:
            return -1
        else:
            return frequency_search(root.l_child, word)     # recursive call if child exists
    return 0

if __name__ == '__main__':
    # local_root = search_node("mystery")
    source_text = sys.argv[1]
    local_root = histogram(source_text)
    # tree_print(local_root)
    search_frequency = frequency_search(local_root, "mystery")
    print("Frequency of 'mystery': " + str(search_frequency))
