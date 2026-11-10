class Solution:
    def sumAndMultiply(self, n: int) -> int:
        word = str(n)
        i = len(word) - 1
        newWord = ''
        while i >= 0:
            if word[i] != '0':
                newWord += word[i]
            i -= 1
        nonZeroWord = newWord[::-1]
        l = len(nonZeroWord) - 1
        summ = 0
        while l >= 0:
            summ += int(nonZeroWord[l])
            l -= 1
        if nonZeroWord == '':
            nonZeroWord = '0'
        answer = int(nonZeroWord) * summ
        return answer
        