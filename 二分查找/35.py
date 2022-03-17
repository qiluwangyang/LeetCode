"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。

示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2

示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1

示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4

示例 4:
输入: nums = [1,3,5,6], target = 0
输出: 0
"""


class Solution:
    def searchInsert1(self, nums, target):
        """
        暴力破解方法，时间复杂度为O(n)
        :param nums:
        :param target:
        :return:
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

    def searchInsert2(self, nums, target):
        """
        二分法求解：区间划分
        :param nums:
        :param target:
        :return:
        """
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


s = Solution()
nums = [1]
target = 2
print(s.searchInsert2(nums, target))
