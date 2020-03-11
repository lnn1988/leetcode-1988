package main

import (
	"fmt"
	"sort"
)

/*
 * @lc app=leetcode.cn id=56 lang=golang
 *
 * [56] 合并区间
 */

// @lc code=start
// @lc code=start

func max(i, j int) int {
	if i >= j {
		return i
	}
	return j
}

func min(i, j int) int {
	if i <= j {
		return i
	}
	return j
}

func merge(intervals [][]int) [][]int {
	re := [][]int{}
	if len(intervals) == 0 {
		return re
	}
	// 排序
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	currentArr := []int{}
	currentArr = append(currentArr, intervals[0][0], intervals[0][1])

	for _, arr := range intervals[1:] {
		if arr[0] <= currentArr[1] {
			curMax := max(currentArr[1], arr[1])
			curMin := min(currentArr[0], arr[0])
			currentArr = append([]int{}, curMin, curMax)
		} else {
			re = append(re, currentArr)
			currentArr = append([]int{}, arr[0], arr[1])
		}
	}
	re = append(re, currentArr)

	return re
}

// @lc code=end
// @lc code=end

func main() {
	intervals := [][]int{}
	intervals = append(intervals, []int{1, 3}, []int{2, 6}, []int{8, 10}, []int{15, 18})
	fmt.Println(merge(intervals))
}
