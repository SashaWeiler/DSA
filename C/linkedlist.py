class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        self.data

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

if __name__ == '__main__':
    llist = LinkedList()
    print(llist)
    
    first_node = Node("a")
    llist.head = first_node
    
    second_node = Node("b")
    third_node = Node("c")
    first_node.next = second_node
    second_node.next = third_node
    
    print(llist)