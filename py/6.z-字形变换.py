#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = []
        for i in range(numRows):
            res.append([])
        flag = False
        currentRow = 0
        for i in s:
            res[currentRow].append(i)
            if currentRow == 0 or currentRow == numRows - 1:
                flag = not(flag)
            if flag:
                currentRow += 1
            else:
                currentRow -= 1
        r = ''
        for i in range(numRows):
            r += ''.join(res[i])
        return r

# @lc code=end

s = "AB"
print(Solution().convert(s, 1))
