"""
nums1中数字x的下一个更大元素是指x在nums2中对应位置右侧的第一个比x大的元素。给你两个没有重复元素的数组nums1和nums2 ，下标从0开始计数，其中
nums1是nums2的子集。对于每个0 <= i < nums1.length ，找出满足nums1[i] == nums2[j]的下标j ，并且在nums2确定nums2[j]的下一个更大元素。
如果不存在下一个更大元素，那么本次查询的答案是 - 1 。
返回一个长度为nums1.length的数组ans作为答案，满足ans[i]是如上所述的下一个更大元素 。

示例1：
输入：nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2].
输出：[-1, 3, -1]
解释：nums1中每个值的下一个更大元素如下所述：- 4 ，用加粗斜体标识，nums2 = [1, 3, 4, 2]。不存在下一个更大元素，所以答案是 - 1 。
- 1 ，用加粗斜体标识，nums2 = [1, 3, 4, 2]。下一个更大元素是3 。- 2 ，用加粗斜体标识，nums2 = [1, 3, 4, 2]。不存在下一个更大元素，所以
答案是 - 1 。

示例2：
输入：nums1 = [2, 4], nums2 = [1, 2, 3, 4].
输出：[3, -1]
解释：nums1中每个值的下一个更大元素如下所述：
    2 ，用加粗斜体标识，nums2 = [1, 2, 3, 4]。下一个更大元素是3 。
    4 ，用加粗斜体标识，nums2 = [1, 2, 3, 4]。不存在下一个更大元素，所以答案是 - 1 。
"""


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        暴力解法
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in nums1:
            for j in range(nums2.index(i), len(nums2)):
                if nums2[j] > i:
                    ans.append(nums2[j])
                    break
                if j == len(nums2) - 1:
                    ans.append(-1)
        return ans

    def nextGreaterElement2(self, nums1, nums2):
        """
        单调栈 +哈希表
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        res = {}
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            res[num] = stack[-1] if stack else -1
            stack.append(num)

        return [res[num] for num in nums1]


nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
s = Solution()
print(s.nextGreaterElement2(nums1, nums2))
