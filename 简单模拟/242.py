"""
给定两个字符串s和t ，编写一个函数来判断t是否是s的字母异位词。注意：若和t中每个字符出现的次数都相同，则称s和t互为字母异位词。

示例1:
输入: s = "anagram", t = "nagaram"
输出: true

示例2:
输入: s = "rat", t = "car"
输出: false
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}
        for i in s:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1

        for j in t:
            if j not in d2:
                d2[j] = 1
            else:
                d2[j] += 1

        print(d1, d2)
        return d1 == d2


s = Solution()
print(s.isAnagram('rat', 'car'))
