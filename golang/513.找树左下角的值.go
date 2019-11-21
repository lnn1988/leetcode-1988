// package main

/*
 * @lc app=leetcode.cn id=513 lang=golang
 *
 * [513] 找树左下角的值
 */

// @lc code=start

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

func findBottomLeftValue(root *TreeNode) (re int) {
	re = root.Val
	trace := []*TreeNode{}
	cur_trace := []*TreeNode{}
	trace = append(trace, root)
	for len(trace) > 0 {
		for i := 0; i < len(trace); i++ {
			if trace[i].Left != nil {
				cur_trace = append(cur_trace, trace[i].Left)
			}
			if trace[i].Right != nil {
				cur_trace = append(cur_trace, trace[i].Right)
			}
		}
		if len(cur_trace) != 0 {
			re = cur_trace[0].Val
		}
		trace = []*TreeNode{}
		for i := 0; i < len(cur_trace); i++ {
			trace = append(trace, cur_trace[i])
		}
		cur_trace = []*TreeNode{}
	}
	return
}

// @lc code=end
// func main() {
// 	node1 := TreeNode{
// 		Val: 1,
// 	}
// 	node2 := TreeNode{
// 		Val: 3,
// 	}
// 	node3 := TreeNode{
// 		Val: 3,
// 	}
// 	node4 := TreeNode{
// 		Val: 4,
// 	}
// 	node5 := TreeNode{
// 		Val: 5,
// 	}
// 	node6 := TreeNode{
// 		Val: 6,
// 	}
// 	node1.Left = &node2
// 	node1.Right = &node3
// 	node2.Left = &node4
// 	node3.Right = &node5
// 	node5.Left = &node6
// 	fmt.Println(findBottomLeftValue(&node1))
// }
