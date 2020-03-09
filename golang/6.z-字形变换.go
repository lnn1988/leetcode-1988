
/*
 * @lc app=leetcode.cn id=6 lang=golang
 *
 * [6] Z 字形变换
 */

// @lc code=start
func convert(s string, numRows int) string {
	if numRows < 2{
		return s
	}

	res := make([]string, numRows)
	flag := false
	currentRow := 0
	for _, i := range s {
		res[currentRow] += string(i)
		if currentRow == 0 || currentRow == numRows-1 {
			flag = !flag
		}
		if flag {
			currentRow ++
		} else {
			currentRow --
		}
	}
	r := ""
	for _, i := range res{
		r += i
	}
	return r
}
// @lc code=end
