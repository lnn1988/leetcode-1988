/*
 * @lc app=leetcode.cn id=1071 lang=golang
 *
 * [1071] 字符串的最大公因子
 */

// @lc code=start
func gcdOfStrings(str1 string, str2 string) string {
	if (str1 + str2) != (str2 + str1) {
		return ""
	}
	// 使 str1 为较长的字符串
	if len(str2) > len(str1) {
		str1, str2 = str2, str1
	}

	l := len(str1) - len(str2)
	if l == 0 {
		return str1
	} else {
		return gcdOfStrings(str1[len(str2):], str2)
	}

}

// @lc code=end

