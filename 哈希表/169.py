"""
给定一个大小为n的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n / 2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例1：
输入：[3, 2, 3]
输出：3

示例2：
输入：[2, 2, 1, 1, 1, 2, 2]
输出：2
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        哈希表
        :type nums: List[int]
        :rtype: int
        """
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1

        l = len(nums) // 2
        for key, value in res.items():
            if value > l:
                return key

    def majorityElement2(self, nums):
        """
        分治
        :type nums: List[int]
        :rtype: int
        """
        pass


s = Solution()
print(s.majorityElement([3, 2, 3]))
