class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            generalW = 0
            daysNeeded = 1  
            mid = (left + right) // 2
            
            for weight in weights:
                generalW += weight
                if generalW > mid:
                    daysNeeded += 1
                    generalW = weight
                    
            if daysNeeded <= days:
                right = mid - 1
            else:
                left = mid + 1

        return left