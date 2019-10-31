from node import Node, get_node_list

def size(head):
    if isinstance(head, Node) and head != None:
        current = head
        count = 0
        while(current.next != None):
            current = current.next
            count += 1

        return count + 1
    return 0

if __name__ == '__main__':
    node = get_node_list(10)

    print('NodeList Size: ', size(node))
