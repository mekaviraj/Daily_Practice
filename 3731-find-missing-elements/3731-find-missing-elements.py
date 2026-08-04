class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        low  = min(nums)
        high = max(nums)
        ans = []
        for i in range(low , high+1) :
            if c[i] != 1 :
                ans.append(i)
        return ans 
