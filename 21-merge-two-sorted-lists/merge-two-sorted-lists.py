# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
            Understand 
                - The idea is to return one singly linked list that merges the two lists

                Questions
                    - Can we have two empty lists?
                    - Can we have a one empty list?

            Match
                - Define a new list

            Plan
                - Check if both lists are empty
                - Check if one of the lists is empty
                - Create an empty node
                - Assign current to the empty node
                - Traverse through the list1 and list2
                - Check what list is not None

            Evaluate
                - Time Complexity: O(n * m) since we traverse through the two lists
                - Space Complexity: O(n) due to the new list created
        """
        if list1 is None and list2 is None:
            return list1
        
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        mergedList = ListNode(0)
        current = mergedList

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
        
        return mergedList.next