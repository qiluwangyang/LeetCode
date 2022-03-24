"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
"""


class Solution(object):
    def canJump(self, nums):
        """
        贪心算法
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        rightmost = 0

        for i in range(n):
            # 循环遍历元素的最大步长所能到的索引
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])  # 更新最远能到达的位置

            if rightmost >= n - 1:  # 当最远能到达的位置超过最后一个元素时，返回True
                return True
        return False


s = Solution()
print(s.canJump(nums=[3, 2, 1, 0, 4]))
