class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        #30 degrees per hour 
        # 6 per minute 
        # minute degrees mminus hour degree minus 0.5*hour

        # ans is min of ans , 360 - ans 
        h = 30
        m = 6
        hm = 0.5
        if hour == 12 :
            hour = 0

        ans = abs(minutes * m  - (hour * 30) - ( hm*minutes))
        # ans2 = 360 - 
        return min(ans , 360 - ans )
