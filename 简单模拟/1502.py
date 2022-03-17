"""
给你一个数字数组arr 。如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为等差数列 。如果可以重新排列数组形成等差数列，请返回
true ；否则，返回false 。

示例1：
输入：arr = [3, 5, 1]
输出：true
解释：对数组重新排序得到[1, 3, 5]或者[5, 3, 1] ，任意相邻两项的差分别为2或 - 2 ，可以形成等差数列。

示例2：
输入：arr = [1, 2, 4]
输出：false
解释：无法通过重新排序得到等差数列。
"""


class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        minus = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != minus:
                return False
        return True





