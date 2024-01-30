class Node():
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def addToHead(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def addToTail(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    def printValues(self):
        temp = self.head
        while temp.next != None:
            print(temp.val)
            temp = temp.next
        print(temp.val)

a = LinkedList()
a.addToHead(1)
a.addToHead(2)
a.addToHead(3)
a.addToTail(4)
a.printValues()