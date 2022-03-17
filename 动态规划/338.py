"""
给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。

示例 1：
输入：n = 2
输出：[0,1,1]
解释：
0 --> 0
1 --> 1
2 --> 10
"""


class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0]
        for i in range(1, n + 1):
            if i % 2 == 0:
                dp.append(dp[i // 2])  # 偶数
            else:
                dp.append(dp[i // 2] + 1)  # 奇数
        return dp


s = Solution()
print(s.countBits(10))
