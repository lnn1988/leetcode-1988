#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        re = False
        fast, slow = head, head
        while (fast and slow and fast.next):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                re = True
                break
        return re



# @lc code=end

