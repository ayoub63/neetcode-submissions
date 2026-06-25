class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        current, prev= head, None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev
            

            

            



        
"""
bin bei head 

nächste node ist nxt nxt pointet zu head also prev sozusagen

dann von nxt zu nxt.next usw.

head -> node -> node 


"""