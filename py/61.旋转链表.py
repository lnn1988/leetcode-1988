#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        if k == 0:
            return head
        
        # 成环
        # n 记录链表长度
        n = 1
        p = head
        while p.next:
            p = p.next
            n += 1
        p.next = head
        head = p.next

        # 新的 head\tail 要移动的位置
        new_tail_num = (n-k)%n-1 + n
        new_head_num = (n-k)%n
        
        new_tail = head
        new_head = head
        for i in range(new_tail_num):
            new_tail = new_tail.next
        for i in range(new_head_num):
            new_head = new_head.next

        new_tail.next = None
        
        return new_head


# @lc code=end


l1 = ListNode(1)
l2 = ListNode(2)
# l3 = ListNode(3)
# l4 = ListNode(4)
# l5 = ListNode(5)
l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5

r = Solution().rotateRight(l1, 2)
while r:
    print(r.val)
    r = r.next