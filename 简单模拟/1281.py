"""
给你一个整数n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。

示例1：
输入：n = 234
输出：15
解释：
各位数之积 = 2 * 3 * 4 = 24
各位数之和 = 2 + 3 + 4 = 9
结果 = 24 - 9 = 15

示例2：
输入：n = 4421
输出：21
解释：
各位数之积 = 4 * 4 * 2 * 1 = 32
各位数之和 = 4 + 4 + 2 + 1 = 11
结果 = 32 - 11 = 21
"""


class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        mul_num = 1
        sum_num = 0

        while n > 0:
            tmp = n % 10
            mul_num = mul_num * tmp
            sum_num = sum_num + tmp
            n = n // 10

        return mul_num - sum_num


s = Solution()
print(s.subtractProductAndSum(4421))
