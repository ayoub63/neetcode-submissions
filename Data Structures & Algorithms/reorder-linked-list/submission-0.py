# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def find_middle(head):
            slow = head
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow
        

        def reverseList(head):
            curr = head
            prev = None 

            while curr:
                following = curr.next
                curr.next = prev
                prev = curr
                curr = following

            return prev

        middle = find_middle(head)
        second = middle.next
        middle.next = None

        second = reverseList(second)
        first = head

        while second:
            curr1 = first.next
            curr2 = second.next

            first.next = second
            second.next = curr1

            first = curr1
            second = curr2


        
