"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {None: None}
        curr = head

        while curr:
            copied_node = Node(curr.val)
            copies[curr] = copied_node
            curr = curr.next

        curr = head

        while curr:
            copies[curr].next = copies[curr.next]
            copies[curr].random = copies[curr.random]
            curr = curr.next

        return copies[head]
            
        

        

        