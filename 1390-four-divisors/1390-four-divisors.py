class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            count = 0
            div_sum = 0
            for d in range(1, int(math.sqrt(n)) + 1):
                if n % d == 0:
                    div_sum += d
                    count += 1
                    if d != n // d:
                        div_sum += n // d
                        count += 1
                    if count > 4:
                        break
            if count == 4:
                total += div_sum
        return total