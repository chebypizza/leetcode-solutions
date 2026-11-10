class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        counter = 0

        for i in range(len(arr1)):
            isSafe = True
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    isSafe = False
                    break
            if isSafe:
                counter += 1

        return counter