# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list.
        
        :param head: The head node of the singly linked list.
        :return: The head node of the reversed singly linked list.
        """

        # If the list is empty, return the head (which is None)
        if head is None:
            return head

        # Initialize previous node as None (this will become the new tail)
        previous = None

        # Initialize current node as the head of the list
        current = head

        # Traverse through the list
        while current:
            # Temporarily store the next node
            next_node = current.next

            # Reverse the current node's pointer
            current.next = previous

            # Move the previous node to this current node
            previous = current

            # Move to the next node in the original list
            current = next_node
        
        # At the end, previous will be the new head of the reversed list
        return previous

        
