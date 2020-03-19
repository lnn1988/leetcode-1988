package main

import "fmt"

/*
 * @lc app=leetcode.cn id=680 lang=golang
 *
 * [680] 验证回文字符串 Ⅱ
 */

// @lc code=start
func helper(s string) bool {
	i := 0
	j := len(s) - 1
	for i < j {
		if s[i] == s[j] {
			i++
			j--
		} else {
			return false
		}
	}
	return true
}

func validPalindrome(s string) bool {
	if len(s) == 1 {
		return true
	}
	i, j := 0, len(s)-1
	for i <= j {
		if s[i] == s[j] {
			i++
			j--
			continue
		} else {
			return helper(s[i:j]) || helper(s[i+1:j+1])
		}
	}
	return true
}

// @lc code=end

func main() {
	s := "abddcba"
	//fmt.Println(helper(s))
	fmt.Println(validPalindrome(s))
}
