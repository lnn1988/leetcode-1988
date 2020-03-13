# 【LeetCode】1004. Max Consecutive Ones III
# 给出一个二进制串和一个整数k，k表示可以将串中的任意k个0换成1，求变换完后能形成的最大连续1串的长度

# 维持一个滑动窗口
# 设置 left, right 分为为窗口的左右边界，保证这个窗口内 0 的个数不会大于 K

def longestOnes(l, k):
    res = 0
    left, right = 0, 0
    change_time = 0

    for right in range(0, len(l)):
        
        if l[right] == 0:
            change_time += 1
        
        if change_time > k:
            while change_time > k:
                left += 1
                if l[left] == 0:
                    left += 1
                    change_time -= 1
        
        res = max(res, right - left + 1)
        print("right ", right, "left ", left, "res ", res)
    return res

l = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(l, k))
