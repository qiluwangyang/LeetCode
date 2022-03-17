"""
给定一个非负整数numRows，生成「杨辉三角」的前numRows行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例1:
输入: numRows = 5
输出: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

示例2:
输入: numRows = 1
输出: [[1]]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 当行数为1时，直接返回[[1]]
        if numRows == 1:
            return [[1]]
        res = []
        for i in range(numRows):
            tmp = []
            for j in range(i + 1):
                # 行数为0或列数为0或行数等于列数时，值为1
                if i == 0 or j == 0 or i == j:
                    tmp.append(1)
                # 否则等于相同列上一行的元素 + 上一列上一行的元素
                else:
                    tmp.append(res[i - 1][j] + res[i - 1][j - 1])
            res.append(tmp)

        return res

    def generate2(self, numRows):
        """
        动态规划
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 边界，必须存在，不然IndexError
        dp = [[1]]
        for i in range(1, numRows):
            # 增加新的一行
            dp.append([1])
            # j需要从1开始，j-1的值才是第一列
            for j in range(1, i):
                # 状态转移方程dp[i][j]=dp[i−1][j−1]+dp[i−1][j]
                dp[i].append(dp[i-1][j-1] + dp[i-1][j])

            # 增加末尾元素
            dp[i].append(1)

        return dp


s = Solution()
print(s.generate2(5))
