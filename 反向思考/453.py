"""
给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。

示例 1：
输入：nums = [1,2,3]
输出：3
解释：只需要3次操作（注意每次操作会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

示例 2：
输入：nums = [1,1,1]
输出：0
"""


class Solution(object):
    def minMoves(self, nums):
        """
        错误解法
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        n = len(nums)
        sum_nums = sum(nums)

        if n == 1 or nums[1:] == nums[:-1]:
            return count

        sum_nums = sum_nums + n - 1
        count += 1
        while sum_nums % n != 0:
            sum_nums = sum_nums + n - 1
            count += 1

        return count

    def minMoves2(self, nums):
        """
        反向思考，n-1个元素+1即有一个元素-1
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        min_num = min(nums)
        for i in nums:
            count += i - min_num
        return count


nums = [3, 1, 3]
s = Solution()
print(s.minMoves2(nums))
