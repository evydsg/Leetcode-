# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
            Understand
                - The idea is to modify the list to return L0 -> L (last node) -> L1 -> L(lastnode -1)

                Questions
                    - Can we have an empty list?
                    - What if the list only has two nodes?
                
            
            Match
                - Fast and slow pointer to find the middle of the list
            
            Plan
                - Use two pointers, slow and fast
                - Traverse through the list while fast is not none
                    - Move the slow once
                    - Move the fast two times
                - Reverse the second part
                - Merge the two halves
        """

        if head is None:
            return 
        
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        current = slow
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        first, second = head, previous

        while second.next:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
            





        