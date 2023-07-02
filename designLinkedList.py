class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0        

    def get(self, index: int) -> int:
        """
        :type index: int
        :rtype: int
        """
        if (index < 0) or (index >= self.size):
            return -1
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.val

    def addAtHead(self, val: int) -> int:
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
        
        

    def addAtIndex(self, index: int, val:int) -> None:
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if (index < 0) or (index > self.size):
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            current = self.head
            for i in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if (index < 0) or (index >= self.size):
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1
