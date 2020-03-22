package main

import "fmt"

/*
 * @lc app=leetcode.cn id=59 lang=golang
 *
 * [59] 螺旋矩阵 II
 */

// @lc code=start
func generateMatrix(n int) [][]int {

	t, b, l, r := 0, n-1, 0, n-1

	num := 1
	tar := n * n
	mat := make([][]int, n)

	for i := 0; i < n; i++ {
		mat[i] = make([]int, n)
	}

	for num <= tar {
		i := l
		for i <= r {
			mat[t][i] = num
			num++
			i++
		}
		t++

		i = t
		for i <= b {
			mat[i][r] = num
			i++
			num++
		}
		r--

		i = r
		for i >= l {
			mat[b][i] = num
			num++
			i--
		}
		b--

		i = b
		for i >= t {
			mat[i][l] = num
			num++
			i--
		}
		l++
	}
	return mat
}

// @lc code=end

func main() {
	n := 3
	fmt.Println(generateMatrix(n))
}
