# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        lastEle = head
        length = 1
        
        while lastEle.next:
            lastEle = lastEle.next
            length += 1
        
        k = k % length
        lastEle.next = head
        
        tempNode = head
        for _ in range(length - k - 1):
            tempNode = tempNode.next
            
        answer = tempNode.next
        tempNode.next = None
        return answer