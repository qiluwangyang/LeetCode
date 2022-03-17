"""
给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi)
总和最大。返回该最大总和 。

示例 1：
输入：nums = [1,4,3,2]
输出：4

思路：
    排序
"""


# 反证法证明贪心解法
# 原答案：nums[k] + nums[k + 2] + ... + nums[n - 1]
# 调整后答案： nums[k + 1] + nums[k + 3] + ... + nums[n - 2] + min(nums[n], nums[k])
#      即nums[k] + nums[k + 1] + nums[k + 3] + ... + nums[n - 2]
# 对比原答案和调整后答案，原答案的每一项都大于等于调整后答案的每一项
class Solution(object):
    def arrayPairSum(self, nums):
        """
        排序
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans

    def arrayPairSum2(self, nums):
        """
        优雅
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])


nums = [1, 4, 3, 2]
s = Solution()
print(s.arrayPairSum2(nums))
