"""
给定由一些正数（代表长度）组成的数组nums ，返回由其中三个长度组成的、面积不为零的三角形的最大周长 。如果不能形成任何面积不为零的三角形，返回0。

示例1：
输入：nums = [2, 1, 2]
输出：5

示例2：
输入：nums = [1, 2, 1]
输出：0
"""


class Solution(object):
    def largestPerimeter(self, nums):
        """
        排序 + 贪心
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        length = 0
        for idx in range(2, len(nums)):
            if nums[idx - 2] - nums[idx - 1] < nums[idx]:
                return nums[idx - 2] + nums[idx - 1] + nums[idx]
        return length


nums = [1, 2, 1]
s = Solution()
print(s.largestPerimeter(nums))
