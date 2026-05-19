class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        dct = {}

        for num in nums1:
            dct[num] = 1

        for num in nums2:
            if num in dct:
                return num

        return -1