# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy_ptr = dummy

        while list1 and list2:
            if list1 and list1.val <= list2.val:
               dummy_ptr.next = list1
               list1 = list1.next
            else:
                dummy_ptr.next  = list2 
                list2 = list2.next

            
            

            dummy_ptr = dummy_ptr.next

        if list1:
            while list1:
                dummy_ptr.next = list1
                list1 = list1.next
        if list2:
            while list2:
                dummy_ptr.next = list2
                list2 = list2.next

        return dummy.next
