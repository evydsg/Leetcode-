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
            return head
        
        temporary = Node(0)
        current = temporary
        stack = [head]

        while stack:
            temp = stack.pop()

            if temp.next:
                stack.append(temp.next)
            if temp.child:
                stack.append(temp.child)
            
            current.next = temp
            temp.prev = current
            temp.child = None
            current = temp
        
        temporary.next.prev = None

        return temporary.next