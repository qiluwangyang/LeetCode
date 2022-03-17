"""
给你两个字符串：ransomNote和magazine ，判断ransomNote能不能由magazine里面的字符构成。如果可以，返回true ；否则返回false 。
magazine中的每个字符只能在ransomNote中使用一次。

示例1：
输入：ransomNote = "a", magazine = "b"
输出：false

示例2：
输入：ransomNote = "aa", magazine = "ab"
输出：false

示例3：
输入：ransomNote = "aa", magazine = "aab"
输出：true
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        效率低下
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return False
        return True

    def canConstruct2(self, ransomNote, magazine):
        """
       哈希表
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for i in magazine:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for i in ransomNote:
            if i in d and d[i] != 0:
                d[i] -= 1
            else:
                return False
        return True