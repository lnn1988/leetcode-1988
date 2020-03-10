#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start

phone_dict = {}
phone_dict["2"] = "abc"
phone_dict["3"] = "def"
phone_dict["4"] = "ghi"
phone_dict["5"] = "jkl"
phone_dict["6"] = "mno"
phone_dict["7"] = "pqrs"
phone_dict["8"] = "tuv"
phone_dict["9"] = "wxyz"

class Solution:
    def letterCombinations(self, digits: str) :
        if not digits :
            return []

        def backtrack(conbination, nxt_digit):
            if len(nxt_digit) == 0:
                res.append(conbination)
                return
            
            for letter in phone_dict[nxt_digit[0]]:
                backtrack(conbination + letter, nxt_digit[1:])
        
        res = []
        backtrack("", digits)
            
        return res

# @lc code=end

digits = "23"
Solution().letterCombinations(digits)