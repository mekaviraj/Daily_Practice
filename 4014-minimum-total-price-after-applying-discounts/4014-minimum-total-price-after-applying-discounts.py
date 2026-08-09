class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse = True)
        discounts.sort(reverse = True)
        p = len(prices)
        d = len(discounts)
        ans = 0
        if p > d :
            for i in range(d) :
                x = (prices[i] * (100 - discounts[i]) ) / 100
                ans += x
                print(x)
            for i in range( d , p) :
                ans += prices[i]
        else :
            for i in range(p) :
                x = (prices[i] * (100 - discounts[i]) ) / 100
                
                ans += x
        # elif p < d: 
        #     for i in range(p) :
        #         x = (prices[i] * (100 - discounts[i]) ) / 100
        #         ans += x
        #     for i in range( p , d) :
        #         ans += prices[i]
        
        return ans 
