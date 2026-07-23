class Solution:
    def maxValue(self, n: str, x: int) -> str:
        # maxi = float("-inf")

        # if n[0] == "-":
        #     for i in range(1, len(n) + 1):
        #         c = n[:i] + str(x) + n[i:]
        #         maxi = max(maxi, int(c))
        # else:
        #     for i in range(len(n) + 1):
        #         c = n[:i] + str(x) + n[i:]
        #         maxi = max(maxi, int(c))

        # return str(maxi)
        if n[0] != "-":
            for i in range(len(n)):
                if int(n[i]) < x:
                    return n[:i] + str(x) + n[i:]
        else:
            for i in range(1, len(n)):
                if int(n[i]) > x:
                    return n[:i] + str(x) + n[i:]
        return n + str(x)