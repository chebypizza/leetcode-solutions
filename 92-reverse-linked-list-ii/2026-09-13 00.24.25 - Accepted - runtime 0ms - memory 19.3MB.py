# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return 

        cur = head
        prev = None
        curIndex = 1

        while cur:
            if curIndex == left:
                beforeStart = prev
                tail = cur

                for _ in range(right - left + 1):
                    nextN = cur.next
                    cur.next = prev
                    prev = cur
                    cur = nextN
                
                tail.next = cur

                if beforeStart:
                    beforeStart.next = prev
                else:
                    return prev
                break

            prev = cur
            cur = cur.next
            curIndex += 1

        return head