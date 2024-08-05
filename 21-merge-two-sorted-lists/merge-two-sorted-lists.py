# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Understand
            - The idea is to merge two sorted lists

            Question
                - Can we have an empty list?
                - Are we always guaranteed to have integers or can we have other type of data?

        Match
            Temporary Head

        Plan
            - Check if both lists are empty
            - Check if either list1 or list2 is empty
            - Initialize a dummy node to simplify the merge process
            - Use a current pointer to build the new list
            - While both lists are not empty
                - Compare the current elements of both lists
                - Attach the smaller element to the new list
                - Move the pointer of the list from which the element was taken
            - If there are remaining elements in either list, attach them to the new list
            - Return the merged list
        """
        # Create a dummy node to help with the merge process
        tempHead = ListNode()
        current = tempHead

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2
        
        return tempHead.next 