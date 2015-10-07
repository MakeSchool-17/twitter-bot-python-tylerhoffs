import sys
import tokenize         # import custom tokenize class


def count_words(tokens):    # function to count unique tokens and update their frequencies
    word_counts = {}
    for i in range(len(tokens)):
        try:
            word_counts[tokens[i]] += 1
        except KeyError:
            word_counts[tokens[i]] = 1
    return word_counts


def heap_creation(word_counts):  # function to create a max heap using the dictionary of words
    heap = []
    num_items = 0
    for key, value in word_counts.items():
        tup = (key, value)
        heap.append(tup)
        num_items += 1
        index = num_items - 1
        parent = (index - 1) // 2
        while heap[parent][1] < heap[index][1]:
            temp = heap[parent]
            heap[parent] = heap[index]
            heap[index] = temp
            index = parent
            parent = (index - 1) // 2
            if parent == -1:
                break
    print(heap)


if __name__ == '__main__':
    # local_root = search_node("mystery")
    source_text = sys.argv[1]
    corpus = open(source_text, encoding='utf-8')
    entire_text = corpus.read()
    corpus.close()
    tokens = tokenize.tokenize_func(entire_text)
    word_counts = count_words(tokens)
    heap_creation(word_counts)
