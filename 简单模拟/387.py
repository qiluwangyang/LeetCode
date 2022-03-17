"""
给定一个字符串s ，找到它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 - 1 。

示例1：
输入: s = "leetcode"
输出: 0

示例2:
输入: s = "loveleetcode"
输出: 2

示例3:
输入: s = "aabb"
输出: -1
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s[i] not in s[:i] and s[i] not in s[i + 1:]:
                return i
        return -1


s = "aabb"
so = Solution()
print(so.firstUniqChar(s))
