// package main

import (
	"fmt"
	"sort"
)

/*
 * @lc app=leetcode.cn id=1 lang=golang
 *
 * [1] 两数之和
 */

// @lc code=start
func twoSum(nums []int, target int) (re []int) {
	if len(nums) < 2{
		return
	}
	m := make(map[int]int, len(nums))
	for i:=0; i<len(nums); i++ {
		cur_v := nums[i]
		cur_tar := target - cur_v
		if v, ok := m[cur_tar]; ok {
			re = append(re, i, v)
			sort.Ints(re)
			return
		} else {
			m[cur_v] = i
		}
	}
	return
}
// @lc code=end

func main()  {
	nums := []int{12, 7, 11, 15}
	target := 19
	fmt.Println(twoSum(nums, target))
}