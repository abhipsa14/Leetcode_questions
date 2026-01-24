class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=0
        rev=0
        m=x
        if x<0:
            return False
        else:
            while(x!=0):
                a=x%10
                rev=rev*10+a
                x=x//10
        return m==rev
