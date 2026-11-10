class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        
        low = 0
        high = len(arr)

        while low < high:
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid + 1
            else:
                high = mid

        left = low - 1
        while len(ans) != k:
            if left < 0:
                ans.append(arr[low])
                low += 1
            elif low == len(arr):
                ans.append(arr[left])
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[low] - x):
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[low])
                low += 1
        ans.sort()

        return ans