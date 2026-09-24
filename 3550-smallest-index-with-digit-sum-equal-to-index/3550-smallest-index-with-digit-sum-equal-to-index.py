class Solution:
    def sumOfdigits(self, num) -> int:
        sum = 0
        num = abs(num)

        while num > 0:
            a = num % 10
            num = num // 10
            sum += a

        return sum

    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if self.sumOfdigits(nums[i]) == i:
                return i

        return -1