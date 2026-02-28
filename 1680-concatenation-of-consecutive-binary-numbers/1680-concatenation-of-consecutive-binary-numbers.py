class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD=10**9+7
        s=''
        b=''
        for i in range(1,n+1):
            b=bin(i)[2:]
            s+=b
        m=int(s,2)%MOD
        return m

