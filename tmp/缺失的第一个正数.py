# 缺失的第一个正数（leetcode第41题）

class Solution:
    def firstMissingPositive(self, nums) -> int:

        if nums == [1]:
            return 2

        find_1 = False
        length = len(nums)
        for i in range(length):
            if nums[i] == 1:
                find_1 = True
            if nums[i] <= 0 or nums[i] > length:
                nums[i] = 1
        
        if find_1 == False:
            return 1

        nums.append(1)
        
        for i in range(length):
            if nums[abs(nums[i])] < 0:
                continue
            else:
                nums[abs(nums[i])] = 0 - nums[abs(nums[i])]
        
        for i in range(1, length+1):
            if nums[i] > 0:
                return i



l = [0, 1, 3, 5, 6]
l = [0, 1, 2, 3, 4]
l = [1, 2, 3, 0]
l = [1]
l = [2, 1]
print(Solution().firstMissingPositive(l))