class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # [1,2,2,3], limit = 3
        people.sort()

        left = 0
        right = len(people) - 1
        ans = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1

            ans += 1   

        return ans