"""
给你两个按非递减顺序排列的整数数组nums1和nums2，另有两个整数m和n ，分别表示nums1和nums2中的元素数目。
请你合并nums2到nums1中，使合并后的数组同样按非递减顺序排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组nums1中。为了应对这种情况，nums1的初始长度为m + n，其中前m个元素表示应合并的元素，后n
个元素为0 ，应忽略。nums2的长度为n 。

示例1：
输入：nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
输出：[1, 2, 2, 3, 5, 6]
解释：需要合并[1, 2, 3]和[2, 5, 6] 。合并结果是[1, 2, 2, 3, 5, 6] ，其中斜体加粗标注的为nums1中的元素。

示例2：
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并[1]和[] 。合并结果是[1] 。

示例3：
输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是[]和[1] 。合并结果是[1] 。注意，因为m = 0 ，所以nums1中没有元素。nums1中仅存的0仅仅是为了确保合并结果可以顺利存放到
nums1中。
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        双指针
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p = q = 0
        res = []
        while p < m and q < n:
            if nums1[p] < nums2[q]:
                res.append(nums1[p])
                p += 1
            else:
                res.append(nums2[q])
                q += 1

        if p == m:
            res += nums2[q:]
        elif q == n:
            # 剩余元素不包括占位值0
            res += nums1[p:m]

        # 将res的值拷贝到nums1数组中
        nums1[:] = res
        return nums1

    def merge2(self, nums1, m, nums2, n):
        """
        逆向双指针
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p, q, now = m - 1, n - 1, m + n - 1
        while p > -1 or q > -1:
            # 当nums1数组中元素消耗完毕，将nums2数组所有元素加入到nums1数组中，q的索引应该减小
            if p == -1:
                nums1[now] = nums2[q]
                q -= 1
            # p的索引减小
            elif q == -1:
                nums1[now] = nums1[p]
                p -= 1
            elif nums1[p] > nums2[q]:
                nums1[now] = nums1[p]
                p -= 1
            else:
                nums1[now] = nums2[q]
                q -= 1
            now -= 1

        return nums1


nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1
s = Solution()
print(s.merge2(nums1, m, nums2, n))
