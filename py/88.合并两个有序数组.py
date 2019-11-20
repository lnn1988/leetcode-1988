#
# @lc app=leetcode.cn id=88 lang=python
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
        
        idx_1, idx_2, idx = m-1, n-1, m+n-1
        while idx_1 >= 0 and idx_2 >= 0:
            if nums1[idx_1] >= nums2[idx_2]:
                nums1[idx] = nums1[idx_1]
                idx_1 -= 1
            else:
                nums1[idx] = nums2[idx_2]
                idx_2 -= 1
            idx -= 1

        if idx_2 >= 0:
            nums1[:idx_2+1] = nums2[:idx_2+1]
# @lc code=end

nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1
Solution().merge(nums1, m, nums2, n)