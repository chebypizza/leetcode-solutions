# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        rest = 0

        while l1 or l2 or rest:
            if l1:
                firstValue = l1.val
                l1 = l1.next
            else:
                firstValue = 0

            if l2:
                secondValue = l2.val
                l2 = l2.next
            else:
                secondValue = 0

            sum = firstValue + secondValue + rest
            rest = sum // 10
            
            cur.next = ListNode(sum % 10)
            cur = cur.next

        return dummy.next