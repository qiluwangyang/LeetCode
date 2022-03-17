"""
给你一个下标从0开始的整数数组nums，该数组的大小为n，请你计算 nums[j]-nums[i] 能求得的最大差值，其中 0<=i<j<n 且 nums[i]<nums[j] 。
返回最大差值 。如果不存在满足要求的 i 和 j ，返回 -1 。
"""


class Solution:
    def maximumDifference(self, nums):
        """
        错误解法
        :param nums:
        :return:
        """
        left = 0
        max_num = -1
        while nums[left:]:
            for i in range(len(nums[left:])):
                if i == len(nums) - 1:
                    return max_num
                if nums[i] > nums[i + 1]:
                    tmp = nums[i] - nums[left]
                    if tmp > max_num:
                        max_num = tmp
                    left = i + 1
        return max_num

    def maximumDifference2(self, nums):
        """
        错误解法，[87,68,91,86,58,63,43,98,6,40]
        :param nums:
        :return:
        """
        left, right = 0, len(nums) - 1
        max_num = -1
        while left < right:
            if nums[left] < nums[right]:
                tmp = nums[right] - nums[left]
                if max_num < tmp:
                    max_num = tmp
                right -= 1
            else:
                left += 1

        return max_num

    def maximumDifference3(self, nums):
        """
        暴力破解
        :param nums:
        :return:
        """
        # index指向当前最小的元素
        index = 0
        res = -1
        for i in range(len(nums)):
            # 当前i指向的元素比index指向的元素大时，进行判断
            if nums[i] > nums[index]:
                # 如果求出的最大值比res存储的最大值大，则进行替换，否则不做操作
                if nums[i] - nums[index] > res:
                    res = nums[i] - nums[index]
            # i指向的元素比index指向的元素小，替换index指向的元素
            else:
                index = i
        return res

    def maximumDifference4(self, nums):
        """
        双指针遍历
        :param nums:
        :return:
        """
        res, max_, min_, tmp = 0, -1, nums[0], 1
        while tmp < len(nums):
            min_ = min_ if min_ < nums[res] else nums[res]
            max_ = max_ if max_ > nums[tmp] - min_ else nums[tmp] - min_
            res += 1
            tmp += 1
        if max_ == 0:
            max_ = -1
        return max_


nums = [1, 5, 2, 10]
s = Solution()
print(s.maximumDifference4(nums))
