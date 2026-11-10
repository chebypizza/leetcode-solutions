class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        left = 0
        right = len(matrix) - 1
        neededArr = []

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                neededArr = matrix[mid]
                break
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                right = mid - 1

        if not neededArr:
            return False

        left = 0
        right = len(neededArr) - 1

        while left <= right:
            mid = (left + right) // 2
            if neededArr[mid] == target:
                return True
            elif neededArr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False