class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        current = self.head
        count = 0

        while current:
            if count == index:
                return current.value
            count += 1
            current = current.next
        
        return -1 

    def addAtHead(self, val: int) -> None:
        newHead = Node(val, self.head)
        self.head = newHead
        

    def addAtTail(self, val: int) -> None:
        newTail = Node(val)
        if self.head is None:
            self.head = newTail
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = newTail

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        count = 0
        current = self.head
        while count < index - 1 and current:
            current = current.next
            count += 1
        
        if current is None:
            return
        
        newNode = Node(val, current.next)
        current.next = newNode


    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        
        count = 0
        current = self.head
        while count < index - 1 and current:
            current = current.next
            count += 1
        
        if current is None or current.next is None:
            return
        
        current.next = current.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)