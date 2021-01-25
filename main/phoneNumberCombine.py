"""
题目：
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
// https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序
"""

import collections
# 题目相对简单，枚举所有的组合即可

class Solution:
    def letterCombinations(self, digits):
        if not digits: return []
        fang, tmp = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                     "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"],
                     "9": ["w", "x", "y", "z"]}, []
        for i in range(len(digits)):
            if i == 0:
                tmp = fang[digits[i]]
            else:
                tmp = [j + k for j in tmp for k in fang[digits[i]]]
        return tmp

# 递归
class Solution2:
    def letterCombinations(self, digits: str):
        ##递归法
        ##特殊情况的处理
        if len(digits)==0:
            return []

        res = [] ##输出结果
        ##1、定义数字对应的字母
        digi_match_alpha = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ##2、写一个递归的函数，digits:传入的数字组合，index：访问的第几个当前的数字，s:每种结果的组合
        def findAlpha(digits,index,s):
            ##递归的终止条件
            if index== len(digits):
                res.append(s)
                return

            digit = digits[index] ##当前的数字
            alphas = digi_match_alpha[digit] ##当前数字对应的字母
            for i in range(len(alphas)):
                findAlpha(digits,index+1,s+alphas[i]) ##递归去找下一个数字对应的字母，s+alphas[i]就是一种组合情况
        ##调用递归函数
        findAlpha(digits,0,"")
        return res


# BFS
class Solution3:
    def letterCombinations(self, digits: str):

        ##先定义数字和字母的字典
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        ##特殊条件判断
        if len(digits) == 0:
            return res
        ##使用BFS来解决
        deque = collections.deque()
        deque.append("")
        for i in range(len(digits)):
            lens_deque = len(deque)
            for j in range(lens_deque):
                curr_digit = dic[digits[i]]
                curr_deque_digit = deque.popleft()
                for digit in curr_digit:
                    deque.append(curr_deque_digit + digit)
            print("当前队列中的内容：", deque)  ##这一句就一下明白每次在干啥了
        return list(deque)

