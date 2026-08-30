# class Solution:
#     def minimumDeletions(self, nums: List[int]) -> int:
#         mini = min(nums)
#         maxi = max(nums)
#         for i in range(len(nums)) :
#             if nums[i] == mini :
#                 minip = i
#             if nums[i] == maxi :
#                 maxip = i
        
#         ans = 0 
#         #way 1  
#         low = min(minip , maxip )
#         hig  = max(minip , maxip) 
#         ans = low + 1 +  ( len(nums)   - 1 - hig )  
#         return ans 

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        i, j, n=nums.index(min(nums)), nums.index(max(nums)), len(nums)
        if i>j: i, j=j, i
        return min(i+1+n-j, j+1, n-i)