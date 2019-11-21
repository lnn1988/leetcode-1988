#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        trace = [root]
        cur_trace = []
        re = root.val
        while trace:
            for node in trace:
                if node.left or node.right:
                    if node.left:
                        cur_trace.append(node.left)
                    if node.right:
                        cur_trace.append(node.right)
            
            if cur_trace == []:
                trace = []
            if cur_trace:
                re = cur_trace[0].val
                trace = cur_trace
                cur_trace = []

        return re
# @lc code=end
root = TreeNode(2)
n1 = TreeNode(1)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(5)
n5 = TreeNode(6)
root.left = n1
root.right = n2
n2.left = n3
n2.right = n4
print(Solution().findBottomLeftValue(root))