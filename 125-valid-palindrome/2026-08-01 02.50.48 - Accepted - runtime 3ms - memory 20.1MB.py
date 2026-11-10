class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = "".join(char for char in s if char.isalnum())
        newStr = newStr.lower()

        return newStr == newStr[::-1]