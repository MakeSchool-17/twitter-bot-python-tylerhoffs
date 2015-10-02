# import re
# import sys


class link_node():                    # class defining the structure for the node of a single linked list
    def __init__(self, key, data):
        self.next = None
        self.key = key
        self.data = data


class linked_list():                # class definiing the structure of a linked list
    def __init__(self):     # constructor function
        self.head = None
        self.tail = None

    def append(self, key, data):        # append function that adds a key and data as a new node
        print(key)
        if self.head is None:
            new_node = link_node(key, data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = link_node(key, data)
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, key):              # delete function that searches for a key and removes the node associated with it
        if self.head is not None:
            curr_node = self.head
            prev_node = None
            while curr_node.next is not None:
                print(curr_node.key)
                if curr_node.key == key:
                    if prev_node is None:
                        self.head = curr_node.next
                    else:
                        prev_node.next = curr_node.next
                else:
                    curr_node = curr_node.next


class custom_hash_table():              # class that defines teh structure of a hash table
    def __init__(self, size):
        self.table = [0] * size
        print(self.table)
        for i in range(size):
            self.table[i] = linked_list()
        print(self.table)
        self.size = size

    def insert(self, key, value):      # insert function that finds the has value of the key and calls the append function the appropriate linked list
        hash_val = hash(key)
        hash_val = hash_val % self.size
        print(hash_val)
        self.table[hash_val].append(key, value)

    def delete(self, key):          # delete function that find the hash value of the key and calls the delete function of the appropriate linked list
        hash_val = hash(key)
        hash_val = hash_val % self.size
        self.table[hash_val].delete(key)

    def print_table(self):          # a function that prints out all of the keys stored in the hash table as well as their positions
        for i in range(0, self.size):
            curr_node = self.table[i].head
            if curr_node is not None:
                print("Node at index " + str(i) + ": " + curr_node.key + " " + str(curr_node.data))
                while curr_node.next is not None:
                    curr_node = curr_node.next
                    print("Node at index " + str(i) + ": " + curr_node.key + " " + str(curr_node.data))


if __name__ == '__main__':
    hash1 = custom_hash_table(3)
    hash1.insert("blah", 4)
    hash1.insert("fish", 3)
    hash1.insert("blue", 4)
    hash1.insert("red", 7)
    hash1.insert("one", 19)
    hash1.insert("two", 2)
    hash1.insert("whatever", 1)
    hash1.print_table()
    hash1.delete("whatever")
    hash1.delete("red")
    hash1.print_table()
