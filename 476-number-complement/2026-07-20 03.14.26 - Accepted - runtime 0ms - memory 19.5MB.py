class Solution:
    def findComplement(self, num: int) -> int:
        num = str(bin(num)[2:])
        i = 0
        newNum = ''
        while i < len(num):
            if num[i] == '0':
                newNum += '1'
            else:
                newNum += '0'
            i += 1
        newNum = int(newNum, 2)
        return newNum