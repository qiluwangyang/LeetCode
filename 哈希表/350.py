"""
给你两个整数数组nums1和nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次
数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

示例1：
输入：nums1 = [1, 2, 2, 1], nums2 = [2, 2]
输出：[2, 2]

示例2:
输入：nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
输出：[4, 9]
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        排序 + 双指针
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()

        l1 = l2 = 0

        res = []
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] == nums2[l2]:
                res.append(nums1[l1])
                l1 += 1
                l2 += 1
            else:
                if nums1[l1] < nums2[l2]:
                    l1 += 1
                else:
                    l2 += 1
        return res

    def intersect2(self, nums1, nums2):
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
            else:
                d[i] += 1

        for j in nums2:
            if j in d and d[j] > 0:
                res.append(j)
                d[j] -= 1

        return res


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
s = Solution()
print(s.intersect2(nums1, nums2))
