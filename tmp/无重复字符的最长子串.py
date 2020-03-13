# 滑动窗口

class Solution(object):
    def allUnique(self, l):
        for i in range(len(l)):
            for j in range(len(l)):
                if i == j:
                    continue
                if l[i] == l[j]:
                    return False
        return True
    
    def lengthOfLongestSubstring(self, l):
        length = len(l) - 1
        left, right = 0, 0
        res = ""
        while right <= length:
            right += 1
            print("right moved ", right)
            unique = self.allUnique(l[left:right+1])
            print(left, right, unique)
            while unique == False and left < right:
                left += 1
                print("left moved ", left)
                unique = self.allUnique(l[left:right+1])
            
            if left == right:
                continue
            print(left, right)
            if len(res) <= len(l[left:right+1]):
                res = l[left:right+1]

            
        
        return res


l = "abcabadse"
print(Solution().lengthOfLongestSubstring(l))
