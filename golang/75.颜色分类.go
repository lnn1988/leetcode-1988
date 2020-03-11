package main

import "fmt"

/*
 * @lc app=leetcode.cn id=75 lang=golang
 *
 * [75] 颜色分类
 */

// @lc code=start
func sortColors(nums []int) []int {
	if len(nums) == 0 {
		return nums
	}
	p0, cur, p2 := 0, 0, len(nums)-1
	for cur <= p2 {
		switch nums[cur] {
		case 0:
			nums[p0], nums[cur] = nums[cur], nums[p0]
			p0++
			cur++
		case 2:
			nums[p2], nums[cur] = nums[cur], nums[p2]
			p2--
		default:
			cur++
		}
	}
	return nums
}

// @lc code=end

func main() {
	i := []int{2, 0, 1}
	fmt.Println(sortColors(i))
}
