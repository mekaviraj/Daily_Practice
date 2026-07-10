class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        def count(arr) :
            x = 0
            for i in arr :
                if i == 1 :
                    x += 1
            return x
        for i in matrix :
            ans.append(count(i))
        return ans 
