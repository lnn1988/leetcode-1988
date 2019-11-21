package main

import "fmt"

func dfs(n int, m int) (re []int) {
	for i := 0; i < 10; i++ {
		cur := n*10 + i
		if cur > m {
			break
		}
		re = append(re, cur)
		r := dfs(cur, m)
		for j := 0; j < len(r); j++ {
			if r[j] > m {
				break
			}
			re = append(re, r[j])
		}
	}
	return
}

func lexicalOrder(n int) (re []int) {
	for i := 1; i < 10; i++ {
		if i > n {
			break
		}
		re = append(re, i)
		r := dfs(i, n)
		for j := 0; j < len(r); j++ {
			if r[j] > n {
				break
			}
			re = append(re, r[j])
		}
	}
	return
}

func main() {
	//n := 13
	fmt.Println(lexicalOrder(100))
}
