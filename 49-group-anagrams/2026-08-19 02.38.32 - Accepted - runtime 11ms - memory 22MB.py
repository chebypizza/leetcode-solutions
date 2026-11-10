class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrDict = defaultdict(list)

        for word in strs:
            sortedWord = "".join(sorted(word))    #ключ-отсортированное слово(sortedWord)
            anagrDict[sortedWord].append(word)   #добавление в словарь слов, которые совпадают при сортировании с ключом

        return list(anagrDict.values())