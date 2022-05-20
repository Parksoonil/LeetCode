"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache = {}
        new_ptr = dummy = Node(-1)
        
        while head:
            if head in cache:
                newnode = cache[head]
            else:
                newnode = Node(head.val)
                cache[head] = newnode
            new_ptr.next = newnode
            new_ptr = new_ptr.next
            
            if head.random:
                if head.random in cache:
                    new_random = cache[head.random]
                else:
                    new_random = Node(head.random.val)
                    cache[head.random] = new_random
                new_ptr.random = new_random
            head = head.next
        return dummy.next
            