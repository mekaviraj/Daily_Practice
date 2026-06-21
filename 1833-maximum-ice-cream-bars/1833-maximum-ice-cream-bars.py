class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0 
        s = 0
        for i in range(len(costs)) :
            s += costs[i]
            if s > coins :
                return ans 
            ans += 1
            
        return ans