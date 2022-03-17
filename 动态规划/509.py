"""
斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定 n ，请计算 F(n) 。
"""


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]

    def fib2(self, n):
        if n < 2:
            return n
        a, b, c = 0, 0, 1
        for i in range(2, n + 1):
            a, b = b, c
            c = a + b
        return c


s = Solution()
print(s.fib2(4))
