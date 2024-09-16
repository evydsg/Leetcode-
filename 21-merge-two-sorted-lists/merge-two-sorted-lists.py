# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return list1
        
        merged = ListNode(0)
        currentM = merged

        while list1 and list2:
            if list1.val > list2.val:
                currentM.next = list2
                list2 = list2.next
            else:
                currentM.next = list1
                list1 = list1.next
            
            currentM = currentM.next
        
        if list1:
            currentM.next = list1
        elif list2:
            currentM.next = list2
        
        return merged.next