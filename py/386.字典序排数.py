#
# @lc app=leetcode.cn id=386 lang=python
#
# [386] 字典序排数
#

# @lc code=start
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        re = []
        for i in range(1, 10):
            if i > n:
                break
            re.append(i)
            r = self.dfs(i, n)
            for j in r:
                if j > n:
                    break
                re.append(j)
        return re

    def dfs(self, n, m):
        re = []
        for i in range(10):
            cur = n*10+i
            if cur > m:
                break
            re.append(cur)
            re.extend(self.dfs(cur, m))
            
        return re
# @lc code=end


print(Solution().lexicalOrder(100))
# print(Solution().dfs(1, 100))