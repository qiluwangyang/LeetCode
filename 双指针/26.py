"""
给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。
由于在某些语言中不能改变数组的长度，所以必须将结果放在数组nums的第一部分。更规范地说，如果在删除重复项之后有 k 个元素，那么 nums 的前 k 个元素应该保存最终结果。
将最终结果插入 nums 的前 k 个位置后返回 k 。
不要使用额外的空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1：
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 题目要求不使用额外空间，此解作废。
        if len(nums) < 2:
            return len(nums), nums

        l = nums[:1]
        for i in range(1, len(nums)):
            if i not in l:
                l.append(i)
        return len(l), l

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 当数组长度为空或者为1时，直接返回数组长度
        if len(nums) < 2:
            return len(nums)

        # 当数组长度大于1时，进行判断
        index = 0
        for i in range(len(nums)):
            # 两个元素不相等时，index指向的下一个元素和当前i指向的元素进行交换，index指向下一个元素
            # 1. 所有元素都不相同，此时无需对元素进行交换
            # 2. 有部分元素重复
            if nums[i] != nums[index]:
                if i - index > 1:
                    nums[i], nums[index + 1] = nums[index + 1], nums[i]
                index += 1

        return index + 1


s = Solution()
print(s.removeDuplicates2([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
