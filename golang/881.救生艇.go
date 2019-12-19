/*
 * @lc app=leetcode.cn id=881 lang=golang
 *
 * [881] 救生艇
 */

// @lc code=start
func numRescueBoats(people []int, limit int) (re int) {
	sort.Ints(people)
	left, right := 0, len(people) - 1
	for left <= right {
		if people[right] + people[left] <= limit {
			left ++
			right --
		} else {
			right --
		}
		re ++
	}
	return
}
// @lc code=end

// @lc code=end

