"""
给定一个包含[0, n]中n个数的数组nums ，找出[0, n]这个范围内没有出现在数组中的那个数。

示例1：
输入：nums = [3, 0, 1]
输出：2
解释：n = 3，因为有3个数字，所以所有的数字都在范围[0, 3]内。2是丢失的数字，因为它没有出现在nums中。

示例2：
输入：nums = [0, 1]
输出：2
解释：n = 2，因为有2个数字，所以所有的数字都在范围[0, 2]内。2是丢失的数字，因为它没有出现在nums中。
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        排序 + 遍历
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for n, num in enumerate(nums):
            if n != num:
                return n
        return len(nums)

    def missingNumber2(self, nums):
        """
        数学运算
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = n * (n + 1) // 2
        arrSum = sum(nums)
        return total - arrSum

    def missingNumber3(self, nums):
        """
        位运算
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for n, num in enumerate(nums):
            xor ^= n ^ num
        return xor ^ len(nums)

    def missingNumber4(self, nums):
        """
        哈希集合
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        for i in range(len(nums) + 1):
            if i not in s:
                return i


nums = [0, 1]
s = Solution()
print(s.missingNumber4(nums))
