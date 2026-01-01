class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        m=0
        for i in digits:
            m+=pow(10,n-1)*i
            n-=1
        m+=1
        digits.clear()
        while(m!=0):
            a=m%10
            digits.append(a)
            m=m//10
        digits.reverse()
        return digits

