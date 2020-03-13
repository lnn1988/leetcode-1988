# 蛇形打印二叉树
# 二叉树的锯齿形层次遍历
# leetcode 103

# bfs 改进
# 遍历方式跟原来一样，只是在遍历得到的数据追加到 re 的时候，做翻转
class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.re = []

    def bfs_optimise(self, node):
        flag = True
        if node == None:
            return
        nodes = [node]
        while nodes:
            new_val = []
            for node in nodes:
                if node:
                    new_val.append(node.val)
                    nodes = nodes[1:]
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if flag:
                self.re.extend(new_val[::-1])
            else:
                self.re.extend(new_val)
            flag = not flag





t1 = Tree(1)
t2 = Tree(2)
t3 = Tree(3)
t4 = Tree(4)
t5 = Tree(5)
t6 = Tree(6)
t7 = Tree(7)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t5.left = t7
s = Solution()
s.bfs_optimise(t1)
print(s.re)