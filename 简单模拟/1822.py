"""
已知函数signFunc(x)将会根据x的正负返回特定值：如果x是正数，返回1 。如果x是负数，返回 - 1 。如果x是等于0 ，返回0 。
给你一个整数数组nums 。令product为数组nums中所有元素值的乘积。返回signFunc(product) 。

示例1：
输入：nums = [-1, -2, -3, -4, 3, 2, 1]
输出：1
解释：数组中所有值的乘积是144 ，且signFunc(144) = 1

示例2：
输入：nums = [1, 5, 0, 2, -3]
输出：0解释：数组中所有值的乘积是0 ，且signFunc(0) = 0

示例3：
输入：nums = [-1, 1, -1, 1, -1]
输出：-1
解释：数组中所有值的乘积是 - 1 ，且signFunc(-1) = -1
"""


class Solution(object):
    def arraySign(self, nums):
        """
        傻瓜式解法
        :type nums: List[int]
        :rtype: int
        """
        ans = 1
        if 0 in nums:
            return 0

        for i in nums:
            ans *= i

        if ans > 0:
            return 1
        else:
            return -1

    def arraySign2(self, nums):
        """
        遍历数组，判断是否存在元素为0，以及小于0的元素的个数
        :type nums: List[int]
        :rtype: int
        """
        negative = 0
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                negative += 1

        return 1 if negative % 2 == 0 else -1