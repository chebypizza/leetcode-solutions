class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for operation in tokens:
            if operation == '+':
                stack[-2] += stack[-1]
                stack.pop()
            elif operation == '-':
                stack[-2] -= stack[-1]
                stack.pop()
            elif operation == '*':
                stack[-2] *= stack[-1]
                stack.pop()
            elif operation == '/':
                stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()
            else:
                stack.append(int(operation))

        return stack[0]