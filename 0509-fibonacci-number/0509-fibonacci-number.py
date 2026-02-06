class Solution:
    def fibo(self,n):
        if n==0 or n==1:
            return n
        return self.fibo(n-1)+self.fibo(n-2)
    def fib(self, n: int) -> int:
        ans=self.fibo(n)
        return ans
        