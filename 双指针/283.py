"""
给定一个数组nums，编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例1:
输入: nums = [0, 1, 0, 3, 12]
输出: [1, 3, 12, 0, 0]

示例2:
输入: nums = [0]
输出: [0]
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        暴力解法，性能极差
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l):
            if nums[i] == 0:
                for j in range(i, l):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
        return nums

    def moveZeroes2(self, nums):
        """
        单循环解法
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums


s = Solution()
print(s.moveZeroes2([0, 1, 0, 3, 12]))
