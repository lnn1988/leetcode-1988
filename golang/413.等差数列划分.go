package main

import "fmt"

/*
 * @lc app=leetcode.cn id=413 lang=golang
 *
 * [413] 等差数列划分
 */

// @lc code=start
func numberOfArithmeticSlices(A []int) int {
	if len(A) < 3 {
		return 0
	}
	length := len(A)
	dp := make([]int, length)

	for i := 2; i < length; i++ {
		if A[i]+A[i-2] == 2*A[i-1] {
			dp[i] += dp[i-1] + 1
		}
	}
	re := 0
	for _, i := range dp {
		re += i
	}
	return re
}

// @lc code=end

func main() {
	s := []int{1, 2, 3, 4}
	fmt.Println(numberOfArithmeticSlices(s))
}
