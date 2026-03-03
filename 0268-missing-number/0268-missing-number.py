class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum1=0
        sum2=0
        for i in nums:
            sum1+=i
        for i in range(0,n+1):
            sum2+=i
        return abs(sum1-sum2)

