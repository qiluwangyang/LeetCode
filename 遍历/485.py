"""
给定一个二进制数组nums ， 计算其中最大连续1的个数。

示例1：
输入：nums = [1, 1, 0, 1, 1, 1]
输出：3
解释：开头的两位和最后的三位都是连续1 ，所以最大连续1的个数是3.

示例2:
输入：nums = [1, 0, 1, 1, 0, 1]
输出：2
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        特殊情况校验失败:
            [0, 0]
            [1, 0]
            [0, 1]
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1 if nums[0] == 1 else 0

        idx = 1
        max_count = 0
        count = 0

        while idx < len(nums):
            if nums[idx] & nums[idx - 1] == 1:
                count += 1
            else:
                count = 0
            max_count = max_count if max_count > count else count
            idx += 1
        return max_count + 1 if max_count else max_count

    def findMaxConsecutiveOnes2(self, nums):
        """
        双指针
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        max_count = 0
        while idx < len(nums):
            tmp = 0
            if nums[idx] == 1:
                for j in range(idx, len(nums)):
                    if nums[j] == 1:
                        tmp += 1
                    else:
                        idx = j
                        break
                    max_count = max_count if max_count > tmp else tmp
                    # 防止元素全为1的场景
                    if j == len(nums) - 1:
                        return max_count
            else:
                idx += 1
        return max_count

    def findMaxConsecutiveOnes3(self, nums):
        """
        遍历，使用两个变量维护最大连续1的个数和当前连续1的个数
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        cur_count = 0
        for i in nums:
            if i == 1:
                cur_count += 1
            else:
                max_count = max(max_count, cur_count)
                cur_count = 0
            max_count = max(max_count, cur_count)
        return max_count

    def findMaxConsecutiveOnes4(self, nums):
        """
        字符串切割
        :type nums: List[int]
        :rtype: int
        """
        str_nums = ''.join(map(str, nums)).split('0')
        return max(map(len, str_nums))


nums = [0, 0, 0]
s = Solution()
print(s.findMaxConsecutiveOnes4(nums))
