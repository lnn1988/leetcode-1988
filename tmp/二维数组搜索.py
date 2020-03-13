# 在一个横向和纵向都是递增的有界二维坐标轴中，如何快速判断某个数是否存在于这个二维坐标中
import numpy as np

class Solution(object):
    def find(self, arr, k):
        m = len(arr)
        if m == 0:
            return None
        n = len(arr[0])
        if n == 0:
            return None

        m, n = arr.shape
        row = 0
        col = n - 1
        # col 列
        # row 行

        while col >= 0 and row <= n-1:
            if arr[row, col] == k:
                return [row, col]
            elif arr[row, col] > k:
                col -= 1
            elif arr[row, col] < k:
                row += 1



arr = [[1,2,3,4,5], [2,3,4,5,6], [3,4,5,6,7], [4,5,6,7,10]]
a = np.array(arr)
print(Solution().find(a, 10))