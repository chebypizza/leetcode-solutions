class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []    #индексы дней, которые не нашли теплый день
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]: #если индекс сегодня больше, чем того дня из вершины стека, то меняем индекс  
                last = stack.pop()      #выталкиваем,пока в стеке меньше текузего
                ans[last] = i - last
            stack.append(i)

        return ans