package main

import "fmt"

/*
 * @lc app=leetcode.cn id=17 lang=golang
 *
 * [17] 电话号码的字母组合
 */

// @lc code=start
var phoneDict map[byte][]string = map[byte][]string{
	'2': {"a", "b", "c"},
	'3': {"d", "e", "f"},
	'4': {"g", "h", "i"},
	'5': {"j", "k", "l"},
	'6': {"m", "n", "o"},
	'7': {"p", "q", "r", "s"},
	'8': {"t", "u", "v"},
	'9': {"w", "x", "y", "z"},
}

func letterCombinations(digits string) []string {
	res := []string{}
	if digits == "" {
		return res
	}
	res = append(res, "")
	for i := 0; i < len(digits); i++ {
		nums := phoneDict[digits[i]]
		pre := res
		res = []string{}
		for _, num := range nums {
			for _, v := range pre {
				res = append(res, v+num)
			}
		}
	}
	return res
}

// @lc code=end

func main() {
	s := "23"
	fmt.Println(letterCombinations(s))
}
