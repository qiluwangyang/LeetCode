"""
给定一个长度为n的整数数组height 。有n条垂线，第i条线的两个端点是(i, 0)和(i, height[i]) 。
找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。返回容器可以储存的最大水量。
说明：你不能倾斜容器。

示例1：
输入：[1, 8, 6, 2, 5, 4, 8, 3, 7]
输出：49
解释：图中垂直线代表输入数组[1, 8, 6, 2, 5, 4, 8, 3, 7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为49。

示例2：
输入：height = [1, 1]
输出：1
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_capacity = 0

        while left < right:
            tmp = min(height[left], height[right]) * (right - left)
            max_capacity = tmp if tmp > max_capacity else max_capacity
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_capacity


s = Solution()
print(s.maxArea([1, 1]))
