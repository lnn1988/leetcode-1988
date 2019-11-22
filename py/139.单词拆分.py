#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s) + 1
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):
            for j in range(0, i):
                print("--j", j, dp[j], s[j:i])
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
            print("i", i, dp[i], s[:i])
        return dp[-1]
# @lc code=end
s = 'pythonpy'
wordDict = ['py', 'thon']
print(Solution().wordBreak(s, wordDict))