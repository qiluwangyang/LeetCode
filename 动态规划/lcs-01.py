"""
小扣打算给自己的 VS code 安装使用插件，初始状态下带宽每分钟可以完成 1 个插件的下载。假定每分钟选择以下两种策略之一:
    - 使用当前带宽下载插件
    - 将带宽加倍（下载插件数量随之加倍）
请返回小扣完成下载 n 个插件最少需要多少分钟。
"""


class Solution(object):
    def leastMinutes(self, n):
        """
        位运算
        :type n: int
        :rtype: int
        """
        ans = 1
        count = 1
        while ans < n:
            ans = ans << 1
            count += 1
        return count

    def leastMinutes2(self, n):
        """
        动态规划
        :param n:
        :return:
        """
        # 使用dp[0]占位置，从dp[1]开始
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + 1, dp[(i + 1) // 2] + 1)
        return dp[n]


s = Solution()
print(s.leastMinutes2(4))
