# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
            Understand
                - The idea is to check if there is a cycle in the Linked List
            
            Match
                - Fast and slow pointer

            Plan
                - Check if the head is none
                    - return false
                - Initialize both slow and fast pointers
                - Traverse through the list using the a while loop and fast pointer
                    - If slow and fast pointers are the same
                        - Return true
                - Return false
        """
        
        if head is None:
            return head
        
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True

        return False