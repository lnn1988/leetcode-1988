#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
# 用栈维护递减数列

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        l = []
        re = {}
        for i in nums2:
            while len(l) > 0:
                if i > l[-1]:
                    tmp_i = l.pop()
                    re[tmp_i] = i
                else:
                    break
            l.append(i)
        r = []
        for i in nums1:
            r.append(re.get(i, -1))
        return r
# @lc code=end

nums1 = [3]
nums2 = [1,3,4,2]
# nums1 = [2,4]
# nums2 = [1,2,3,4]
print(Solution().nextGreaterElement(nums1, nums2))