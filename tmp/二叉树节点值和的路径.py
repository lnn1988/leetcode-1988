import copy

class treeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self, n):
        # 保存路径
        self.n = n
        self.re = []

    def dfs(self, node, current_sum, current_road):
        if node == None:
            return
        current_sum += node.val
        current_road.append(node.val)

        a = copy.deepcopy(current_road)
        b = copy.deepcopy(current_road)


        if node.left:
            self.dfs(node.left, current_sum, a)
        if node.right:
            self.dfs(node.right, current_sum, b)
        if node.left or node.right:
            return
        if current_sum == self.n:
            self.re.append(current_road)
            return
        if current_sum > self.n:
            return


t1 = treeNode(1)
t2 = treeNode(2)
t3 = treeNode(3)
t4 = treeNode(6)
t5 = treeNode(5)
t1.left = t2
t1.right = t3
t2.left = t4
t3.right = t5
s = Solution(9)
s.dfs(t1, 0, [])
print(s.re)
