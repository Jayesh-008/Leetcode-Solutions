class Solution(object):
    def findWordsContaining(self, words, x):
        b = []
        n = len(words)
        for i in range(0,n):
            if x in words[i]:
                b.append(i)
        return b
