"""
给定一个整数num，将其转化为7进制，并以字符串形式输出。

示例1:
输入: num = 100
输出: "202"

示例2:
输入: num = -7
输出: "-10"
"""


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        flag = False
        if num == 0:
            return "0"

        if num < 0:
            flag = True
            num = 0 - num
        while num != 0:
            res.append(str(num % 7))
            num = num // 7

        if flag:
            return '-' + ''.join(res[::-1])
        return ''.join(res[::-1])

    def convertToBase72(self, num):
        """
        优雅
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)
        digits = []

        while num:
            digits.append(str(num % 7))
            num //= 7

        if negative:
            digits.append("-")

        return ''.join(reversed(digits))


s = Solution()
print(s.convertToBase7(101))
