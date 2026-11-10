# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        #пока не закончится одна половина вставлять элементы поочередно
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #надо развернуть slow.next
        prev = None
        cur = slow.next
        slow.next = None  #отрезать вторую половину

        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur         #начало второй половины после цикла(prev)
            cur = nextNode

        first = head
        second = prev #указать в while, т к будет на 1 меньше мб
        
        while second:
            nextNode1 = first.next   #first tail
            nextNode2 = second.next    #second tail 
            first.next = second       #1st node -> second 
            second.next = nextNode1     #2nd node -> first tail
            first = nextNode1
            second = nextNode2