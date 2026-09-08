class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        half = n//2
        # print(n , half )
        # half1 = sum(nums[:half])
        # half2 =  sum(nums) - half1
        # ans = 0 if half1 <= half2 else 1
        # for i in range( half +1) :
        #     half1 -= nums[i]
        #     # half1 += nums[i+half]
        #     # half2 -= nums[half + i]

        #     # half2 += nums[i]
            
        #     # if half1 > half2 : 
        #     #  ans += 1
        #     half1 -= nums[i - 1]
        #     half1 += nums[(i + half - 1) % n]

        #     half2 = sum(nums) - half1

        #     if half1 > half2:
        #         ans += 1 

        total = sum(nums)
        half1 = sum(nums[:half])

        ans = 1 if half1 > total - half1 else 0

        for i in range(1, n):
            half1 -= nums[i - 1]
            half1 += nums[(i + half - 1) % n]

            if half1 > total - half1:
                ans += 1

        return ans 