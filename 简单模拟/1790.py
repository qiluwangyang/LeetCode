"""
给你长度相等的两个字符串s1和s2 。一次字符串交换操作的步骤如下：选出某个字符串中的两个下标（不必不同），并交换这两个下标所对应的字符。
如果对其中一个字符串执行最多一次字符串交换就可以使两个字符串相等，返回true ；否则，返回false 。

示例1：
输入：s1 = "bank", s2 = "kanb"
输出：true
解释：例如，交换s2中的第一个和最后一个字符可以得到"bank"

示例2：
输入：s1 = "attack", s2 = "defend"
输出：false
解释：一次字符串交换无法使两个字符串相等

示例3：
输入：s1 = "kelb", s2 = "kelb"
输出：true
解释：两个字符串已经相等，所以不需要进行字符串交换

示例4：
输入：s1 = "abcd", s2 = "dcba"
输出：false
"""


class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        暴力解法
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        diff = 0
        cmp = []
        if len(s1) != len(s2):
            return False

        l = len(s1)
        for i in range(l):
            if s1[i] != s2[i]:
                diff += 1
                cmp.extend([s1[i], s2[i]])
        if diff == 0:
            return True
        elif diff == 2:
            return cmp[0] == cmp[-1] and cmp[1] == cmp[-2]
        else:
            return False

    def areAlmostEqual2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        diff = 0
        idx = 0
        s1 = list(s1)
        s2 = list(s2)
        if len(s1) != len(s2):
            return False

        l = len(s1)
        for i in range(l):
            if s1[i] != s2[i]:
                diff += 1
                if diff == 1:
                    idx = i

            if diff == 2:
                s1[idx], s1[i] = s1[i], s1[idx]
                return s1 == s2
        return s1 == s2


s1 = "bank"
s2 = "kanb"
s = Solution()
print(s.areAlmostEqual2(s1, s2))
