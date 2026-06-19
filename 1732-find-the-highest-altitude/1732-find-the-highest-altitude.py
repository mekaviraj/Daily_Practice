class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0 , 0)
        m = -101
        for i in range(1, len(gain)) :
            gain[i] += gain[i-1]
            # m = max(gain[i] , m )
        # print(gain)
        return max(gain)

