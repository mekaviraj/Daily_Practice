class Solution:
    def maxProduct(self, n: int) -> int:
        n = str(n)
        ans = 0
        seen = []
        for i in range(len(n)) :
            if i in seen :
                continue
            else :
                seen.append(i)
            for j in range(i+1 , len(n)) :
                z = int(n[i]) * int(n[j])
                if z > ans :
                    ans = z
        return ans