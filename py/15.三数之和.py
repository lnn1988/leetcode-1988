#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start


class Solution:
    def threeSum(self, nums):
        re = []
        nums.sort()
        print (nums)
        for i in range(len(nums)):
            cur_v = nums[i]
            cur_tar = 0 - cur_v
            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur_s = nums[left] + nums[right]
                if cur_s < cur_tar:
                    left += 1
                elif cur_s > cur_tar:
                    right -= 1
                else:
                    cur_re = [nums[i], nums[left], nums[right]]
                    if not cur_re in re:
                        re.append(cur_re)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return re
# @lc code=end


nums = [-1, 0, 1, 2, -1, -4]
nums = [0, 0, 0, 0]
nums = [-2, 0, 1, 1, 2]
nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
