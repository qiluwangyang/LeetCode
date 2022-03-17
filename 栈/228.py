"""
给定一个  无重复元素 的 有序 整数数组 nums 。
返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于
nums 的数字 x 。
列表中的每个区间范围 [a,b] 应该按如下格式输出：
    "a->b" ，如果 a != b
    "a" ，如果 a == b
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        双指针
        :type nums: List[int]
        :rtype: List[str]
        """
        left = 0
        ans = []
        nums.append(2 ** 32)
        for right in range(1, len(nums)):
            if nums[right] - nums[right - 1] == 1:
                right += 1
            else:
                if right - left == 1:
                    ans.append("%d" % nums[left])

                else:
                    ans.append("%d->%d" % (nums[left], nums[right - 1]))
                left = right
                right += 1
        return ans

    def summaryRanges2(self, nums):
        """
        单调栈哨兵节点
        :type nums: List[int]
        :rtype: List[str]
        """
        # 保证最后一次将所有区域全部计算
        nums.append(2 ** 32)
        ret, start = [], 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                if i - 1 == start:
                    ret.append(str(nums[start]))
                else:
                    ret.append(f"{nums[start]}->{nums[i - 1]}")
                start = i
        return ret


nums = []
s = Solution()
print(s.summaryRanges(nums))
