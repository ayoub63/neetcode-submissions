class Node:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        count = 0
        curr = self.head.next
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        
        return -1
        

    def insertHead(self, val: int) -> None:
        dummyNode = Node(val)
        dummyNode.next = self.head.next
        self.head.next = dummyNode
        if not dummyNode.next:
            self.tail = dummyNode

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0 
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
           if curr.next == self.tail:
            self.tail = curr 
           curr.next = curr.next.next
           return True
        return False 

    def getValues(self) -> List[int]:
        curr = self.head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next

        return res
