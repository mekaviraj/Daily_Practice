class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        ss , ds = 0 , 0
        for i in str(n) :
            i = int(i)
            ss += (i*i)
            ds += i
        
        return (ss - ds) >= 50  