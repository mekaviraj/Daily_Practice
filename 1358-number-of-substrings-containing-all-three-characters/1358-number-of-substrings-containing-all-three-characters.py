class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # ans = 0
        # l = 0
        # r = 2
        # hm = {"a" : 0 , "b" : 0 , "c" : 0 }
        # for i in range(3) :
        #  hm[s[i]] +=1 
        # # while l <= r and r < len(s) -1 : 
        # #     if ( hm["a"] and hm["b"] and hm["c"]) :
        # #         ans +=1 
        # #         r +=1
        # #         hm[s[r]] += 1
        # #     else :
        # #         hm[s[l]] -= 1
        # #         l +=1
        # # return ans 
        # for r in range(len(s)):
        #     hm[s[r]] += 1

        #     while hm["a"] > 0 and hm["b"] > 0 and hm["c"] > 0:
        #         ans += len(s) - r
        #         hm[s[l]] -= 1
        #         l += 1

        # return ans
        count = {"a": 0, "b": 0, "c": 0}
        l = 0
        ans = 0
        n = len(s)

        for r in range(n):
            count[s[r]] += 1

            while count["a"] > 0 and count["b"] > 0 and count["c"] > 0:
                ans += n - r
                count[s[l]] -= 1
                l += 1

        return ans