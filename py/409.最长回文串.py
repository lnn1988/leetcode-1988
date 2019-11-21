#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s):
        count = {}
        re = 0
        for i in s:
            count[i] = count.get(i, 0) + 1
        has_1 = False
        for k, v in count.items():
            if v >= 2:
                re += int(v/2)*2
                count[k] = v-int(v/2)*2
        for k, v in count.items():
            if v == 1:
                has_1 = True
                re += 1
                break
        return re

        
# @lc code=end
s = "ccc"
print(Solution().longestPalindrome(s))
