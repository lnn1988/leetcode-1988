// package main

import (
	"strings"
)

/*
 * @lc app=leetcode.cn id=151 lang=golang
 *
 * [151] 翻转字符串里的单词
 */

// @lc code=start
func reverseWords(s string) string {
	str := strings.Split(s, " ")
	rev_str := []string{}
	for i := len(str) - 1; i >= 0; i-- {
		if len(str[i]) != 0 {
			rev_str = append(rev_str, str[i])
		}
	}
	return strings.Join(rev_str, " ")
}

// @lc code=end

// func main()  {
// 	s := "i mmm  good"
// 	fmt.Println(reverseWords(s))
// }