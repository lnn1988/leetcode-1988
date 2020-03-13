# 从矩阵的左下角走到右上角，即(0,0)->(m,n)，每次只准向右或向上，一共几种走法？（DP）时间复杂度？

# 这个题目其实是一个组合问题。对方向编号，向上是0，向右是1，
# 那么从左下角走到右上角一定要经过M 个1和N个0。
# 这个题目可以转化为从M+N个盒子中挑出M个盒子有多少种方法。


# 动态规划
import numpy as np
def run(m, n):
    dp = np.zeros(dtype = int, shape = (m, n))
    dp[0][0] = 0
    for i in range(1, m):
        dp[i][0] = 1
    for i in range(1, n):
        dp[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

print(run(4, 2))