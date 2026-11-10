class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if -asteroid > stack[-1]:
                    stack.pop()
                    continue
                elif -asteroid == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack