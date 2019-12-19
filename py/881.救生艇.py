#
# @lc app=leetcode.cn id=881 lang=python3
#
# [881] 救生艇
#

# @lc code=start


class Solution:
    def numRescueBoats(self, people, limit):
        re = 0
        p_sort = sorted(people)
        left, right = 0, len(p_sort) - 1
        while right >= left:
            if p_sort[right] + p_sort[left] <= limit:
                re += 1
                right -= 1
                left += 1
            else:
                re += 1
                right -= 1
        return re


# # @lc code=end
# people = [3, 2, 2, 1]
# limit = 3
# print(Solution().numRescueBoats(people, limit))