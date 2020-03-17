package main

import "fmt"

/*
 * @lc app=leetcode.cn id=32 lang=golang
 *
 * [32] 最长有效括号
 */

// @lc code=start

func longestValidParentheses(s string) int {
	stack := []int{-1}
	re := 0
	for i := range s {
		if len(stack) == 0 || stack[len(stack)-1] == -1 {
			stack = append(stack, i)
			continue
		}
		if string(s[i]) == ")" && string(s[stack[len(stack)-1]]) == "(" {
			stack = stack[:len(stack)-1]
			if i-stack[len(stack)-1] > re {
				re = i - stack[len(stack)-1]
			}
			continue
		}
		stack = append(stack, i)
	}
	return re
}

// @lc code=end

func main() {
	s := "()(()"
	fmt.Println(longestValidParentheses(s))
	s = "(()"
	fmt.Println(longestValidParentheses(s))
	s = ")()())"
	fmt.Println(longestValidParentheses(s))
}
