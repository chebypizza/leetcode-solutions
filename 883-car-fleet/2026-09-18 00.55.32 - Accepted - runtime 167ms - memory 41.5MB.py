class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        stack = []

        for pos, spd in cars:
            cur = (target - pos) / spd
            if not stack or cur > stack[-1]:
                stack.append(cur)

        return len(stack)