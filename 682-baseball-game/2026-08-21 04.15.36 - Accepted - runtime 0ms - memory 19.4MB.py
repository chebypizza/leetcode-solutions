class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if not operations:
            return 0

        stack = []

        for cur in operations:
            if cur == '+':
                stack.append(stack[-1] + stack[-2])
            elif cur == 'C':
                stack.pop()
            elif cur == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(cur))

        return sum(stack)