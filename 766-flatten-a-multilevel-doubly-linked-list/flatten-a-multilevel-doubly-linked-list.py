"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return 
        
        newList = Node(0)
        temp = newList
        current = head
        stack = [current]

        while stack:
            multiL = stack.pop()

            if multiL.next:
                stack.append(multiL.next)
            if multiL.child:
                stack.append(multiL.child)
            
            temp.next = multiL
            multiL.prev = temp
            temp = temp.next
            temp.child = None

        newList.next.prev = None

        return newList.next

        