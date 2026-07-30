class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word) == 1 :
            return 1
        else:
            if len(word) <= 8 :
                return len(word)
            else :
                n = len(word) - 8
                ans = 8
                press =  2 
                while n > 8 :    
                    ans += ( press * 8 )
                    press += 1
                    n -= 8 
                ans += ( press * n)

                # ans = (s * 8  )+ (n * s)
                return ans
                