class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        ans = float("-inf") 

        if len(nums) < 6 :
            for i in range(len(nums)) :
                for j in range(i +1, len(nums)) :
                    for k in range(j +1 , len(nums)) :
                        ans = max( ans   , nums[i] * nums[k ] * nums[j])
            return ans
        else :

         nums.sort()
        # a b c d e f 
         i, j , k = 0 , 1 , 2 
         while i > - 4 :
            ans = max( ans   , nums[i] * nums[k ] * nums[j])
            i -= 1 
            j -= 1 
            k -= 1 
         return ans 