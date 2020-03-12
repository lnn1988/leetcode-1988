#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071] 字符串的最大公因子
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2) != (str2 + str1):
            return ""
        
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        l = len(str1) - len(str2)
        if l == 0:
            return str1
        else:
            return self.gcdOfStrings(str1[len(str2):], str2)
# @lc code=end

str1 = "ABC"
str2 = "ABCABC"
print(Solution().gcdOfStrings(str1, str2))
