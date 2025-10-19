class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3=''
        m=len(word1)
        n=len(word2)
        if n>m:
            max_len=n
        else:
            max_len=m
        for i in range(0,max_len):
            if i<len(word1):
                word3=word3+word1[i]
            if i<len(word2):
                word3=word3+word2[i]
        
        return word3
