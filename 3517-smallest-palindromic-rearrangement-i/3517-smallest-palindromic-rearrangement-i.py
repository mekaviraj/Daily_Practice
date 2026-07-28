class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
            # its even 
        half = len(s)// 2
        text = s[:half]
        st= ''.join(sorted(text))
            # c = Counter()
            # for i in range(half) :
        rev = st[::-1]
        if len(s) % 2 == 0 :
            return st + rev
        else :
            return st +s[half]+ rev

