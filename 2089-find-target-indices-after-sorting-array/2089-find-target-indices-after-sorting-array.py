class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        lst=[]
        for i in range(0,len(nums)):
            if(nums[i]==target):
                lst.append(i)
        return lst        