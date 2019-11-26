#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) < 2:
            return []
        m = {}
        res = []
        for i in range(len(nums)):
            cur_v = nums[i]
            cur_tar = target - cur_v
            if cur_tar in m:
                res = [m.get(cur_tar), i]
                res.sort()
                return res
            else:
                m[cur_v] = i
        return res


        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
# @lc code=end


nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))