from collections import Counter
import random
class Solution:
    def __init__(self, nums: List[int]):
        self.nums  = nums 
        self.c = Counter(nums)
        self.sss = {}
        for i in range(len(nums)) :
            if nums[i] not in self.sss :
                self.sss[nums[i]] = [i]
            else :
                self.sss[nums[i]].append(i)

    def pick(self, target: int) -> int:
        # if self.c[t]  == 1 :
        #     return 0
        # else :


            # return self.sss[target].random.choice()
        
            return random.choice(self.sss[target])
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)