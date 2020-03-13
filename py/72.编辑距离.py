#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
import numpy as np
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m == 0:
            return n
        if n == 0:
            return m
        dp = np.zeros((m+1, n+1), dtype=int)
        for i in range(m+1):
            dp[i][0] = i
        for i in range(n+1):
            dp[0][i] = i
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1, j-1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return int(dp[m][n])
# @lc code=end

