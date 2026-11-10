class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]

        ans = []

        def backtrack(curList, index):
            if index == len(digits):
                ans.append("".join(curList))
                return

            for i in range(len(phoneMap[int(digits[index])])):
                curList.append(phoneMap[int(digits[index])][i])
                backtrack(curList, index + 1)
                curList.pop()
        
        backtrack([], 0)
        return ans