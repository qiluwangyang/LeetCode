"""
给你一个非空数组，返回此数组中第三大的数 。如果不存在，则返回数组中最大的数。

示例1：
输入：[3, 2, 1]
输出：1
解释：第三大的数是1 。

示例2：
输入：[1, 2]
输出：2
解释：第三大的数不存在, 所以返回最大的数2 。

示例3：

输入：[2, 2, 3, 1]
输出：1
解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。此例中存在两个值为2的数，它们都排第二。在所有不同数字中排第三大的数为1 。
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        排序 + 集合
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return max(nums)
        else:
            return nums[-3]

    def thirdMax2(self, nums):
        """
        排序
        :type nums: List[int]
        :rtype: int
        """
        # reverse为True表示逆序排列
        nums.sort(reverse=True)
        diff = 1  # 比较3个元素需要比较2次，所以diff初始值从1开始
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                diff += 1

            if diff == 3:
                return nums[i]
        return nums[0]


s = Solution()
print(s.thirdMax2([1, 2]))
