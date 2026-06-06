from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        leftsum = [0] * n
        rightsum = [0] * n

        # Compute left sums
        for i in range(1, n):
            leftsum[i] = leftsum[i - 1] + nums[i - 1]

        # Compute right sums
        for i in range(n - 2, -1, -1):
            rightsum[i] = rightsum[i + 1] + nums[i + 1]

        # Compute result
        result = [0] * n
        for i in range(n):
            result[i] = abs(leftsum[i] - rightsum[i])

        return result