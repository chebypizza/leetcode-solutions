class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        finalAnswer = 0                                                 #5, 3, 2,  4 - > 5(stack[-1]), 3(depth),  4(height[i])

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                depth = stack.pop()
                if not stack:
                    break
                width = i - stack[-1] - 1
                waterHeight = min(height[stack[-1]], height[i]) - height[depth]
                finalAnswer += width * waterHeight
            stack.append(i)

        return finalAnswer