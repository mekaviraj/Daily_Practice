class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if (n * 9) < s :
            return -1
        elif s == 0 :
            return 0
        else :
            ans = "9" * n
            ans = int(ans)
            def ss(n) :
                n = str(n)
                ans = 0
                for i in n :
                    ans += int(i)
                return ans
            
            while ans :
                if ss(ans) == s  :
                    return ans
                ans -= 1

            return ans 

