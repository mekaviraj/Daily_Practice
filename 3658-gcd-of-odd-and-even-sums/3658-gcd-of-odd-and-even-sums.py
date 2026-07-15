class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        e  = 0
        two = 2
        for i in range(n) :
            e += two
            two +=2 

        # print(e, o )
        return gcd(e, n*n)