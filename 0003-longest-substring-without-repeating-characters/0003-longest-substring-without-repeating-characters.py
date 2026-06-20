class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ht= Counter("qwertyuioplkjhgfdsazxcvbnm")
        # l = 0
        # r = 1
        # ans = r - l
        # ht[s[l]] +=1
        # ht[s[r]] +=1
        # while l <= r  and (r < len(s) ):
        #     if ht[s[r]] > 1 :
        #         ht[s[l]] -=1
        #         l +=1
        #     else :
        #         ht[s[r]] += 1
        #         ans = max(ans , r - l -1 )
        #     print(ans)
            # r +=1 
        ht = Counter()
        l = 0
        ans = 0

        for r in range(len(s)):
            ht[s[r]] += 1

            while ht[s[r]] > 1:
                ht[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans 
 
             