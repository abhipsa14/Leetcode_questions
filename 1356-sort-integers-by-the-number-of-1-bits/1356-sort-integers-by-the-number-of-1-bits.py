class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        lst=[[] for _ in range(15)]
        for num in arr:
            bits=bin(num).count('1')
            lst[bits].append(num)
        ans=[]
        for bucket in lst:
            bucket.sort()
            for num in bucket:
                ans.append(num)
        return ans