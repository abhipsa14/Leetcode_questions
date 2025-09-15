class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s=text.split(' ')
        n=len(s)
        cnt=0
        for i in range(0,n):
            for j in brokenLetters:
                if j in s[i]:
                    break
            else:
                cnt+=1
        return cnt
