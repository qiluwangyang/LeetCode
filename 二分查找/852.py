"""
符合下列属性的数组arr称为山脉数组 ：
    arr.length >= 3
    存在i（0 < i < arr.length - 1）使得：
        arr[0] < arr[1] < ... arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
给你由整数组成的山脉数组arr ，返回任何满足arr[0] < arr[1] < ...arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]的
下标i 。

示例1：
输入：arr = [0, 1, 0]
输出：1

示例2：
输入：arr = [0, 2, 1, 0]
输出：1
"""


class Solution:
    def peakIndexInMountainArray1(self, arr):
        """
        二分法查找第一个小于nums[mid]的值的索引
        :param arr:
        :return:
        """
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
        # 返回left和right是等价的
        return left

    def peakIndexInMountainArray2(self, arr):
        """
        顺序查找，题目没有要求时间复杂度
        :param arr:
        :return:
        """
        for index in range(len(arr)):
            if arr[index] > arr[index + 1]:
                return index


s = Solution()
arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
print(s.peakIndexInMountainArray2(arr))
