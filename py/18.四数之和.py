#
# @lc app=leetcode.cn id=18 lang=python
#
# [18] 四数之和
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.getFourSum(nums, target)
    def getFourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums.sort()
        print(nums)
        re = []
        # 固定两个数 nums[i], nums[j]
        # 使指针左右移动
        for i in range(0, len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1
                
                while left < right:
                    cur_target = target - nums[i] - nums[j]
                    cur_sum = nums[left] + nums[right]
                    print([i, j, left, right, cur_sum, cur_target])
                    if cur_sum < cur_target:
                        left += 1
                    if cur_sum > cur_target:
                        right -= 1
                    if cur_sum == cur_target:
                        re.append([nums[i], nums[j], nums[left], nums[right]])
                        break
        return re







# @lc code=end

nums = [1, 0, -1, 0]
target = 0
print(Solution().fourSum(nums, target))