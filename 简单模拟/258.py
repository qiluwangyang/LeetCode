"""
给定一个非负整数num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

示例1:
输入: num = 38
输出: 2
解释: 各位相加的过程为：
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
由于2是一位数，所以返回2。

示例2:
输入: num = 0
输出: 0
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = sum(map(int, list(str(num))))

        return num


s = Solution()
print(s.addDigits(378))
