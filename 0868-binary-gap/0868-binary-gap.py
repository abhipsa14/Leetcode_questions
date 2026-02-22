class Solution:
    def binaryGap(self, n: int) -> int:
        num=bin(n)[2:]
        last=-1
        maxi=0
        for i in range(len(num)):
            if num[i]=='1':
                if last!=-1:
                    maxi=max(maxi,i-last)
                last=i
        return maxi