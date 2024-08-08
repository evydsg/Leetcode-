# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
            Understand
                - The idea is to check if the tail points to a another node instead of being null

                Questions
                    - Can we get an empty list?
                    - Is it possible to have two cycles within one list?
                    - What should we return if the list is empty? False?

            Match  
                - Two pointers: fast and slow
            
            Plan
                - Check if the list is empty
                    if head is none: return None
                - Initialize two pointers: fast and slow
                - Traverse through the list
                    - Move the fast two times
                    - Move the slow one time
        """
        if head is None:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
            
        return False
        