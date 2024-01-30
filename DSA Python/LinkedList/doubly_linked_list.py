class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def addToHead(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
    
    def addToTail(self, val):
        new_node = Node(val)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next
    
    def addToIndex(self, index, val):
        new_node = Node(val)

        if index == 0:
            self.addToHead(val)
            return

        if index < 0:
            return -1

        temp = self.head
        i = 0

        while temp and i < index:
            prev_val = temp
            temp = temp.next
            i += 1

        if i != index:
            return -1

        if temp is None:
            self.addToTail(val)
            return

        prev_val.next = new_node
        new_node.prev = prev_val
        new_node.next = temp
        temp.prev = new_node

    def remove_index(self):
        pass
    
    def printValues(self):
        temp = self.head
        while temp.next:
            print(temp.val)
            temp = temp.next
        print(temp.val)

a = LinkedList()
a.addToHead(1)
a.addToHead(2)
a.addToHead(3)
a.addToTail(4)
a.addToIndex(2, 7)
a.printValues()
