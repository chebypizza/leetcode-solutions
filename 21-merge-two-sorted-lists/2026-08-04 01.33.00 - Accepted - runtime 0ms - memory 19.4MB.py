# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(0)    #Создание узла с первым и пока единственным элементом ноль
        cur = start

        while list1 and list2: #пока не пустые
            if list1.val > list2.val: #значения в листах
                cur.next = list2     #присоединяем элемент листа 2 к cur
                list2 = list2.next    #переходим к следующему элементу в листе 2
            else:
                cur.next = list1     #присоединяем элемент листа 1 к cur
                list1 = list1.next    #переходим к следующему элементу в листе 1
            cur = cur.next      #передвинуть поинтер cur к следущему, только что созданному узлу(line 13, 16)
        
        if list1:       #если не пуст
            cur.next = list1     #прикрепляем остаток  листа1 к cur
        else:
            cur.next = list2   #приклепляем остаток листа2 к cur

        return start.next    #т к cur  улетел в конец, то возварщаем start.next(не start, а именно start.next т к первый элемент нашего нового листа это ноль(line8))