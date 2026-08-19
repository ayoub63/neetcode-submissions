# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy_ptr = dummy

        while list1 or list2:
            if list1 and list1.val <= list2.val:
               dummy_ptr.next = list1
               list1 = list1.next
            else:
                dummy_ptr.next  = list2 
                list2 = list2.next

            if list2 and list2.val <= list1.val:
               dummy_ptr.next = list2
               list2 = list2.next

            else:
                dummy_ptr.next  = list1
                list1 = list1.next


            dummy_ptr = dummy_ptr.next

        return dummy.next
