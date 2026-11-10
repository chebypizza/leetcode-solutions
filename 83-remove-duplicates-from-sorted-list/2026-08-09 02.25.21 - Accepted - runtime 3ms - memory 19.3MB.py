# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        newSet = set()
        cur = head

        while cur and cur.next:
            newSet.add(cur.val)
            if cur.next.val in newSet:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head