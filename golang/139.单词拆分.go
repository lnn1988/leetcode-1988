// package main

import "fmt"

/*
 * @lc app=leetcode.cn id=139 lang=golang
 *
 * [139] 单词拆分
 */

// @lc code=start
// 声明 dp
// dp[i] 为 i 之前的词符合要求(包括)
// 则 dp[i] = max( (dp[j] and s[j:i] in words) for j < i)
func inList(s string, wordList []string) (re bool) {
	for i:=0; i<len(wordList); i++ {
		if wordList[i] == s {
			re = true
		}
	}
	return
}

func wordBreak(s string, wordDict []string) bool {
    n := len(s) + 1
    dp := make([]bool, n)
    dp[0] = true
	for i:=1; i<n; i++ {
		for j:=0; j<i; j++ {
			if dp[j] && inList(s[j:i], wordDict) {
				dp[i] = true
			}
		}
	}
    return dp[n-1]
}
// @lc code=end

func main()  {
	s := "pythonpy1"
	wordDict := []string{"py", "thon"}
	fmt.Println(wordBreak(s, wordDict))
}