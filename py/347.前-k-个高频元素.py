#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start

import heapq
class Solution:
    def topKFrequent(self, nums, k):
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        pq = list()
        for key, value in d.items():
            if len(pq) < k:
                heapq.heappush(pq, (value, key))
            else:
                heapq.heappush(pq, (value, key))
                heapq.heappop(pq)
        re = []
        for i in pq:
            re.append(i[-1])
        return re


# @lc code=end

