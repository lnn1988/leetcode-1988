package main

import (
	"fmt"
	"sort"
)

/*
 * @lc app=leetcode.cn id=455 lang=golang
 *
 * [455] 分发饼干
 */

// @lc code=start
func findContentChildren(g []int, s []int) int {
	sort.Ints(g)
	sort.Ints(s)
	lenG := len(g)
	lenS := len(s)
	i := 0
	j := 0
	r := 0
	for i < lenG && j < lenS {
		if g[i] <= s[j] {
			r++
			i++
			j++
			continue
		}
		j++
	}
	return r
}

// @lc code=end

func main() {
	g := []int{2, 1}
	s := []int{1, 2, 3}
	g = []int{1, 2, 3}
	s = []int{1, 1}
	fmt.Println(findContentChildren(g, s))
}
