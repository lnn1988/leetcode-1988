package main

import (
	"fmt"
)

/*
 * @lc app=leetcode.cn id=61 lang=golang
 *
 * [61] 旋转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.

 */

// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil {
		return head
	}
	// n 记录长度
	// 成环
	n := 1
	p := head
	for p.Next != nil {
		p = p.Next
		n++
	}
	p.Next = head

	newTailNum := (n-k)%n - 1 + n
	newHeadNum := (n-k)%n + n
	//newTail := &ListNode{Val:head.Val, Next:head.Next}
	//newHead := &ListNode{Val:head.Val, Next:head.Next}

	newTail := head
	newHead := head

	for i := 0; i < newTailNum; i++ {
		newTail = newTail.Next
	}
	for i := 0; i < newHeadNum; i++ {
		newHead = newHead.Next
	}
	newTail.Next = nil
	return newHead
}

// @lc code=end

func main() {
	l1 := &ListNode{Val: 0}
	l2 := &ListNode{Val: 1}
	l3 := &ListNode{Val: 2}
	//l4 := &ListNode{Val:4}
	l1.Next = l2
	l2.Next = l3
	//l3.Next = l4
	l := rotateRight(l1, 4)
	for l != nil {
		fmt.Println(l.Val)
		l = l.Next
	}
}
