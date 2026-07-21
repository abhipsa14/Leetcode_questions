class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count={}
        for i in range(len(magazine)):
            count[magazine[i]]=count.get(magazine[i],0)+1
        
        for ch in ransomNote:
            if ch in count and count[ch]>0:
                count[ch]-=1
            else:
                return False
        return True