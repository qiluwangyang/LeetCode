"""
给定一个整数数组，找出总和最大的连续数列，并返回总和。

示例：
输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        动态规划
        :type nums: List[int]
        :rtype: int
        """
        ans = [nums[0]]
        # TODO 优化逻辑，使用常量存储
        for i in range(1, len(nums)):
            ans.append(max(ans[i - 1] + nums[i], nums[i]))

        return max(ans)


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
