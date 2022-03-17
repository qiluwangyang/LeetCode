"""给你一个整数数组nums 。如果任一值在数组中出现至少两次 ，返回true ；如果数组中每个元素互不相同，返回false 。

示例1：
输入：nums = [1, 2, 3, 1]
输出：true

示例2：
输入：nums = [1, 2, 3, 4]
输出：false

示例3：
输入：nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
输出：true
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        超时
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return False
        for i in range(len(nums)):
            if nums[i] in nums[i + 1:]:
                return True

        return False

    def containsDuplicate2(self, nums):
        """
        哈希
        :type nums: List[int]
        :rtype: bool
        """
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 1
            else:
                return True
        return False
