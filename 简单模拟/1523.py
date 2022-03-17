"""
给你两个非负整数low和high 。请你返回low和high之间（包括二者）奇数的数目。

示例1：
输入：low = 3, high = 7
输出：3
解释：3到7之间奇数数字为[3, 5, 7] 。

示例2：
输入：low = 8, high = 10
输出：1
解释：8到10之间奇数数字为[9] 。
"""


class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        else:
            return (high - low) // 2 + 1


s = Solution()

low = 8
high = 10
print(s.countOdds(low, high))
