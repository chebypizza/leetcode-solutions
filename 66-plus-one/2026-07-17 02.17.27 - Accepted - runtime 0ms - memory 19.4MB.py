class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        i = l - 1
        if len(digits) > 1:
            if digits[-1] < 9:
                digits[-1] += 1
            else:
                while i > 0:
                    if digits[i] == 9:
                        digits[i] = 0
                        digits[i - 1] += 1
                    else:
                        digits[i] = 0
                        digits[i - 1] += 1
                    if digits[i - 1] - 1 != 9:
                        break
                    i -= 1
                if digits[0] == 10:
                    digits[0] = 0
                    digits.insert(0, 1)
        else:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            digits.insert(0, 1)
        return digits