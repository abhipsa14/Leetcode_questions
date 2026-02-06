class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        l=1
        i=0
        j=0
        while(j<n):
            maxi=nums[j]
            mini=nums[i]
            while(i<j and maxi>k*mini):
                i+=1
                mini=nums[i]
            l=max(l,j-i+1)
            j+=1
        return n-l

        