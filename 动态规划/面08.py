"""
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结
果模1000000007。

示例1:
 输入：n = 3
 输出：4
 说明: 有四种走法
"""


class Solution(object):
    def waysToStep(self, n):
        """
        动态规划转移方程：dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
        超出时间限制
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 2, 4]
        for i in range(4, n + 1):
            dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

        return dp[n] % 1000000007

    def waysToStep2(self, n):
        """
        优化
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        elif n == 3:
            return 4

        a, b, c, res = 1, 2, 4, 0
        for i in range(4, n + 1):
            res = (a + b + c) % 1000000007     # 对结果进行求余
            a, b, c = b, c, res % 1000000007   # 同余定理， a mod m == b mod m == (a+b) mod m

        return res % 1000000007


s = Solution()
print(s.waysToStep2(900750))
