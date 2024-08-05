# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            Understand
                - The idea is to remove duplicates from the list

                Questions
                    - Can we have an empty list?
                    - Are we always guaranteed to have duplicates?
                
            Match
                - Fast pointer
                - Slow pointer
            
            Plan
                - Check if head is None
                    - Yes, return None
                - Initialize temporary pointers to both point at the head
                    - fast pointer
                - Have a while loop to run while fast pointer is not none
                    - If slowpointer and fast pointer are the same
                        - Move only the fast pointer
                    - Else
                        Next pointer of slow points to fast
                        Move both pointers
                - Return Head
            
            Evaluate
               - Time Complexity: O(n)
               - Space Complexity: O(1)
        """
        if head is None:
            return None
        
        slow = head
        fast = head

        while fast:
            if slow.val == fast.val:
                fast = fast.next
            else:
                slow.next = fast
                slow = slow.next
                fast = fast.next
        slow.next = None
        
        return head