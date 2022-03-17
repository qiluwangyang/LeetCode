"""
给你一个整数数组nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组:是数组中的一个连续部分。

示例1：
输入：nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
输出：6
解释：连续子数组[4, -1, 2, 1]的和最大，为6 。

示例2：
输入：nums = [1]
输出：1
"""


class Solution(object):
    def maxSubArray1(self, nums):
        """
        动态规划
        :type nums: List[int]
        :rtype: int
        """
        # 记录动态规划边界
        if len(nums) == 1:
            return nums[0]

        max_sum = cur_sum = nums[0]
        # 状态转移函数dp[i] = max(nums[i], nums[i] + dp[i - 1])
        for i in range(1, len(nums)):
            cur_sum = max(cur_sum + nums[i], nums[i])
            max_sum = max_sum if max_sum > cur_sum else cur_sum

        return max_sum

    def maxSubArray2(self, nums):
        """
        分治法
        :type nums: List[int]
        :rtype: int
        """
        pass

    def maxSubArray3(self, nums):
        """
        暴力求解：超时
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        for i in range(len(nums)):
            tmp_sum = 0
            for j in range(i, len(nums)):
                tmp_sum += nums[j]
                if tmp_sum > max_sum:
                    max_sum = tmp_sum

        return max_sum
