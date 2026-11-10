class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxAns = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                last = stack.pop()
                height = heights[last]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                maxAns = max(maxAns, height * width)
            stack.append(i)

        #остатки в стеке
        i = len(heights)
        while stack:
            last = stack.pop()
            height = heights[last]
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            maxAns = max(maxAns, height * width)

        return maxAns