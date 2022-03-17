"""
泰波那契序列 Tn 定义如下：
T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

示例 1：
输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
"""


class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
        return dp[n]

    def tribonacci2(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 1]
        if n < 3:
            return dp[n]

        a, b, c, d = 0, 0, 1, 1
        for i in range(3, n + 1):
            a, b, c = b, c, d
            d = a + b + c

        return d


s = Solution()
print(s.tribonacci2(25))
