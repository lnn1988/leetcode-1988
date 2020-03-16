package main

import "fmt"

/*
 * @lc app=leetcode.cn id=496 lang=golang
 *
 * [496] 下一个更大元素 I
 */

// @lc code=start
func nextGreaterElement(nums1 []int, nums2 []int) []int {
	re := make(map[int]int, len(nums2))
	r := make([]int, 0)
	l := make([]int, 0)
	for _, i := range nums2 {
		for len(l) != 0 {
			curI := l[len(l)-1]
			if curI < i {
				re[curI] = i
				l = l[:len(l)-1]
			} else {
				break
			}
		}
		l = append(l, i)
	}

	for _, i := range nums1 {
		if j, ok := re[i]; ok {
			r = append(r, j)
		} else {
			r = append(r, -1)
		}
	}
	return r
}

// @lc code=end

func main() {
	nums1 := []int{4, 1, 2}
	nums2 := []int{1, 3, 4, 2}
	fmt.Println(nextGreaterElement(nums1, nums2))

}
