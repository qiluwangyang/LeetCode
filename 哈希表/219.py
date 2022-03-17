"""
给你一个整数数组nums和一个整数k ，判断数组中是否存在两个不同的索引i和j ，满足nums[i] == nums[j]且abs(i - j) <= k 。
如果存在，返回true ；否则，返回false 。

示例1：
输入：nums = [1, 2, 3, 1], k = 3
输出：true

示例2：
输入：nums = [1, 0, 1, 1], k = 1
输出：true

示例3：
输入：nums = [1, 2, 3, 1, 2, 3], k = 2
输出：false
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        哈希表
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        res = {}
        for i in range(len(nums)):
            if nums[i] not in res:
                res[nums[i]] = i
            else:
                # 当存在相同元素时，判断索引间距是否小于等于k值
                if i - res[nums[i]] <= k:
                    return True
                # 索引间距大于k值时更新键值
                res[nums[i]] = i
        return False


nums = [1, 2, 3, 1, 2, 3]
k = 2
s = Solution()
print(s.containsNearbyDuplicate(nums, k))
