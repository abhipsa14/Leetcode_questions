class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        one=[]
        two=[]

        for i in range(len(nums)):
            if nums[i]==1:
                one.append(i)
            elif nums[i]==2:
                two.append(i)
        if len(one)==0 or len(two)==0:
            return -1
        else:
            ans=float('inf')
            for i in range(len(one)):
                for j in range(len(two)):
                    ans=min(ans,abs(one[i]-two[j]))
            return ans


        