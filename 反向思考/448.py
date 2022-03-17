"""
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式
返回结果。

示例 1：
输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]

示例 2：
输入：nums = [1,1]
输出：[2]

"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        暴力解法，超时
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) + 1
        nums = list(set(nums))
        res = []
        for i in range(1, n):
            if i not in nums:
                res.append(i)

        return res

    def findDisappearedNumbers2(self, nums):
        """
        哈希集合
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        ans = []
        for i in range(1, len(nums) + 1):
            if i not in s:
                ans.append(i)
        return ans

    def findDisappearedNumbers3(self, nums):
        """
        原地修改，给数组中数字索引增加n，然后小于n的索引即答案
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            nums[(num - 1) % len(nums)] += len(nums)
        return [i for i, num in enumerate(nums, 1) if num <= len(nums)]

    def findDisappearedNumbers4(self, nums):
        """
        原地修改，给数组中数字索引取反，然后大于0的索引即答案
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            nums[abs(num) - 1] = - abs(nums[abs(num) - 1])
        return [i for i, num in enumerate(nums, 1) if num > 0]


nums = [4, 3, 2, 7, 8, 2, 3, 1]
s = Solution()
print(s.findDisappearedNumbers4(nums))
