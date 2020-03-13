#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, int(i/2+1)):
                dp[i] = max(max(dp[j], j)*max(dp[i-j], i-j), dp[i])
        
        return dp[n]
        
# @lc code=end

print(Solution().integerBreak(10))