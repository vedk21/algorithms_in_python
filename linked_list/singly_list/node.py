# define node class
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


# helper fucntions

def get_node_list(size):
    node = Node(0)
    refNode = node
    for i in range(1, size):
        newNode = Node(i)
        refNode.next = newNode
        refNode = newNode
    return node
