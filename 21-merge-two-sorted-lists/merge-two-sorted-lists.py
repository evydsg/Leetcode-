# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
            Understand
                The idea is to merge two lists into one and sorted?

                Can we get empty lists?
                Are we always guaranteed to get a sorted list?
            
            Match
                LinkedList
            
            Plan
                Check if any of the lists is empty
                Create a temporary node
                Iterate through the lists while both have them have a value
                    Compare current value of both lists to find the lowest
                        Move the lowest to the next node and assign the current node
                Check if any of the lists still have values
                Return the temporary node.next
        """
        if list1 is None and list2 is None:
            return list1

        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        merged_list = ListNode(0)
        current_merged_list = merged_list

        while list1 and list2:
            if list1.val < list2.val:
                current_merged_list.next = list1
                list1 = list1.next
            else :
                current_merged_list.next = list2
                list2 = list2.next
            
            current_merged_list = current_merged_list.next
        
        if list1:
            current_merged_list.next = list1
        elif list2:
            current_merged_list.next = list2
        
        return merged_list.next
