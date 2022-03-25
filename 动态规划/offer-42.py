"""
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。

示例1:
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        动态规划转移方程：dp[n] = max(dp[n-1] + nums[n], nums[n])
        :type nums: List[int]
        :rtype: int
        """
        dp = [nums[0]] + [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)


s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(nums))
