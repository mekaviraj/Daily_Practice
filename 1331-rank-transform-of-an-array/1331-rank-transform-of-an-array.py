class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = []
        if not arr :
            return arr
        for i in range(len(arr)) :
            a.append([i, arr[i]])
        
        a.sort(key = lambda x : x[1])
        ans = [None] * len(arr)
        temp = a[0][1] 
        ans[a[0][0]] = 1
        counter = 1
        for i in range(1, len(arr)) :
            if a[i][1] == temp :
                ans[a[i][0]] = counter
            else :
                counter += 1
                ans[a[i][0]] = counter
                temp = a[i][1]
        return ans 
        