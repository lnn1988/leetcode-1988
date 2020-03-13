# 连续整数求和(leetcode 第 829 题)，要求时间复杂度小于O(N)
# 假设(x+1)+(x+2)+...+(x+k) = N,
# 即 2N = k(2x+k+1)
# 则: (k<2N)^(1/2)

class Solution(object):
    def consecutiveNumbersSum(self, n):
        k = 1
        res = 0
        while k*k < 2*n:
            x = (2*float(n)/k - 1 - k)/2
            if x == float(int(x)) and x >= 0:
                res += 1
            k += 1
        
        return res

print(Solution().consecutiveNumbersSum(9))