from node import Node, get_node_list

def traverse(head):
    if isinstance(head, Node) and head != None:
        current = head
        list = []
        list.append(current.val)
        while(current.next != None):
            current = current.next
            list.append(current.val)

        return list

if __name__ == '__main__':
    node = get_node_list(10)

    print('NodeList is: ', traverse(node))
