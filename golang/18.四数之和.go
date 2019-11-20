package main

import (
	"fmt"
	"sort"
)

func solution(nums []int, target int) (re [][]int) {
	if len(nums) < 4 {
		return
	}

	sort.Ints(nums)
	for i := 0; i < len(nums)-3; i++ {
		for j := i + 1; j < len(nums)-2; j++ {
			left := j + 1
			right := len(nums) - 1
			cur_target := target - nums[i] - nums[j]
			cur_sum := nums[left] + nums[right]
			fmt.Println(i, j, left, right, cur_sum, cur_target)
			if cur_sum > cur_target {
				right--
			} else if cur_sum < cur_target {
				left++
			} else {
				cur_re := []int{}
				cur_re = append(cur_re, nums[i], nums[j], nums[left], nums[right])
				re = append(re, cur_re)
			}
		}
	}
	return
}

func main() {
	nums := []int{0, 1, -1, 0}
	target := 0
	fmt.Println(solution(nums, target))
}
