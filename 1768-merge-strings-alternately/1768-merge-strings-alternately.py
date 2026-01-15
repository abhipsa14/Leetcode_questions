class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        m=len(word1)
        n=len(word2)
        if m>n:
            maxlen=m
        else:
            maxlen=n
        for i in range(0,maxlen):
            if i<len(word1):
                s=s+word1[i]
            if i<len(word2):
                s=s+word2[i]
        return s