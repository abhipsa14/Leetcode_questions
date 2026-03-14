class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set=set()
        n=len(nums)
        longest=0
        for i in range(0,n):
            my_set.add(nums[i])
        for num in my_set:
            if num-1 not in my_set:
                x=num
                count=1
                while x+1 in my_set:
                    count+=1
                    x+=1
                longest=max(longest,count)
        return longest