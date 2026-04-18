class Solution:
    def mirrorDistance(self, n: int) -> int:
        def rev(n):
            rev=0
            a=0
            while n>0:
                a=n%10
                rev=rev*10+a
                n=n//10
            return rev  
        return abs(n-rev(n))