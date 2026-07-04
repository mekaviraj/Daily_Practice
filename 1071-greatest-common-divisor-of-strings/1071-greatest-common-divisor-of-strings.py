class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n , m = len(str1) , len(str2)
        cd = []

        def cdf(n , m ) :
            for i in range(1 , min(n, m ) +1 ) :
                if n % i == 0 and m % i == 0 :
                    cd.append(i)
        cdf(n, m)
        cd = cd[::-1]
        ans = ""
        al = 0
        def cc(x  , s) :
            a = ""
            while len(a) < len(s) :
                a = a + x
                if a == s :
                 return True
            return False
        
        for i in cd :
            s = str1[:i]

            if cc(s , str1) and cc(s , str2) :
                if len(s) > len(ans) :
                    ans = s
        
        return ans 
              