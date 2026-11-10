# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        k = 0

        while cur:
            cur = cur.next
            k += 1

        target = k - n

        if target == 0:
            return head.next

        cur = head

        for i in range(target - 1):
            cur = cur.next
        
        cur.next = cur.next.next

        return head