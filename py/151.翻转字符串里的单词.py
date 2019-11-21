#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([s for s in s.split(' ')[::-1] if s != ''])
# @lc code=end

s = "a good   example"
print(Solution().reverseWords(s))