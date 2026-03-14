class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos=[]
        neg=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        nums=[]
        for i in range(0,n):
            m=int(i/2)
            if i%2==0:

                nums.append(pos[m])
            else:
                nums.append(neg[m])
        return nums