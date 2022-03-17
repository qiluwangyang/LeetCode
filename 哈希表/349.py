"""
给定两个数组nums1和nums2 ，返回它们的交集 。输出结果中的每个元素一定是唯一的。我们可以不考虑输出结果的顺序 。

示例1：
输入：nums1 = [1, 2, 2, 1], nums2 = [2, 2]
输出：[2]

示例2：
输入：nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
输出：[9, 4]
解释：[4, 9]也是可通过的
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        暴力解法
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            if i in nums2 and i not in res:
                res.append(i)
        return res

    def intersection2(self, nums1, nums2):
        """
        哈希表
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        res = []

        for i in nums1:
            if i not in d:
                d[i] = 1

        for j in nums2:
            if j in d and j not in res:
                res.append(j)

        return res


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

s = Solution()
print(s.intersection2(nums1, nums2))
