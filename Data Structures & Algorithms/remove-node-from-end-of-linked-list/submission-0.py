# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        limit = n
        curr = head
        index = 0
        dummy = ListNode()
        dummy.next = head
        while index < limit - 1 and curr:
            curr = curr.next
            index += 1

        if curr and curr.next:
            curr.next = curr.next.next

        return dummy.next


        

        