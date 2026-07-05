class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        def dr(x) :
            s  = list(str(x))
            m = max(s)
            mi = min(s)
            return int(m) - int(mi)
        hm = {}
        for i in nums :
            x = dr(i)
            if x not in hm :
                hm[x] = [i]
            else :
                hm[x].append(i)
        x  = sum(hm[max(hm.keys())])
        return x