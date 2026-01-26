class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n=len(arr)
        lst=[]
        arr.sort()
        diff=float('inf')
        for i in range(1,n):
            diff=min(diff,arr[i]-arr[i-1])
        for i in range(1,n):
            if arr[i]-arr[i-1]==diff:
                lst.append([arr[i-1],arr[i]])
        return lst
            

