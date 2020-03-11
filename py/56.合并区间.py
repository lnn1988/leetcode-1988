#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals):
        if intervals == []:
            return []
        intervals.sort(key = lambda x:x[0])
        re = []
        cur_arr = intervals[0]
        for i in intervals[1:]:
            
            if i[0] <= cur_arr[1]:
                cur_arr[0] = min(cur_arr[0], i[0])
                cur_arr[1] = max(cur_arr[1], i[1])
            else:
                re.append(cur_arr)
                cur_arr = i
        re.append(cur_arr)
        return re


# @lc code=end

i = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(i))