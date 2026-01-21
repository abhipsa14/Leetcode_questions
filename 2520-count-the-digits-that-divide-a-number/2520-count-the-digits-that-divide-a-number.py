class Solution:
    def countDigits(self, num: int) -> int:
        n=num
        a=0
        lst=[]
        cnt=0
        while n!=0:
            a=n%10
            lst.append(a)
            n=n//10
        for i in lst:
            if num % i==0:
                cnt+=1
        return cnt

            