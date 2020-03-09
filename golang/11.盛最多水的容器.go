/*
 * @lc app=leetcode.cn id=11 lang=golang
 *
 * [11] 盛最多水的容器
 */
// @lc code=start
 func Min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}

func Max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}


func maxArea(height []int) int {
	if len(height) == 0 {
		return 0
	}
	head, tail := 0, len(height) - 1
	re := (tail - head) * Min(height[head], height[tail])
	for head < tail {
		re = Max(re, (tail-head)*Min(height[head], height[tail]))
		if height[head] > height[tail] {
			tail --
		} else {
			head ++
		}
	}
	return re
}
// @lc code=end
