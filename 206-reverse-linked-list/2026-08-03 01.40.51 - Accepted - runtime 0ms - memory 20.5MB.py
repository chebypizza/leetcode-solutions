# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previousNode = None  #Переменная prev изначально равна None, потому что первый узел исходного списка станет самым последним узлом в развернутом списке.У любого последнего узла в односвязном списке указатель на следующий элемент (next) всегда должен смотреть в «никуда» — то есть в None.
        currentNode = head   #->1

        while currentNode:    #Перебор всего списка до конца
            nextNode = currentNode.next      #-> 2
            currentNode.next = previousNode      #Якобы разворот стрелки с "1 -> 2" на "2 -> 1"
            previousNode = currentNode               #Обозначение прошлого элемента
            currentNode = nextNode           #Переход к следующему элементу

        return previousNode                  ##Возвраащем именно prev, т к после всех разворотов стрелок мы придем поменяем направление всего листа и, следовательно, если мы начнем с 1ого элемента, то мы не сможем перейти к next, т к пути(стрелки) просто нет, поэтому начинаем с самого конца, т е prev(также prev находится на один шаг позади cur, т е на самом последнем узле исходного списка).