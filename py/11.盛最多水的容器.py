#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height):
        head, tail = 0, len(height) - 1
        re = (tail-head) * min(tail, head)
        while tail > head :
            
            re = max(re, (tail-head) * min(height[tail], height[head]))
            if height[head] > height[tail]:
                tail -= 1
            else:
                head += 1
        return re
# @lc code=end

# print(Solution().maxArea([2,3,4,5,18,17,6]))