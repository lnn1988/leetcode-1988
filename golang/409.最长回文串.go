package main

import "fmt"

/*
 * @lc app=leetcode.cn id=409 lang=golang
 *
 * [409] 最长回文串
 */

// @lc code=start
func longestPalindrome(s string) (re int) {
	count := make(map[string]int)
	for i:=0; i<len(s); i++  {
		ss := string(s[i])
		count[ss] = count[ss] + 1
	}
	for i:=0; i<len(s); i++ {
		ss := string(s[i])
		if count[ss] >= 2{
			re += int(count[ss]/2)*2
			count[ss] = count[ss] - int(count[ss]/2)*2
		}
	}
	for i:=0; i<len(s); i++ {
		ss := string(s[i])
		if count[ss] == 1{
			re += 1
			break
		}
	}

    return
}
// @lc code=end

func main()  {
	a := "ccc"
	fmt.Println(longestPalindrome(a))
}