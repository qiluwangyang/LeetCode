"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例 1：
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        边界情况：第一行和第一列
        动态规划转移方程：dp[m][n] = min(dp[m-1][n], dp[m][n-1]) + grid[m][n]
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        res = [[0] * n for _ in range(m)]

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    res[i][j] = grid[i][j]  # 起始位置
                elif i == 0:
                    res[i][j] = res[i][j - 1] + grid[i][j]  # 处理第一行
                elif j == 0:
                    res[i][j] = res[i - 1][j] + grid[i][j]  # 处理第一列
                else:
                    res[i][j] += min(res[i - 1][j], res[i][j - 1]) + grid[i][j]  # 处理非边界情况
        return res[-1][-1]

    def minPathSum2(self, grid):
        """
        官方题解
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]

        # 处理第一行
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # 处理第一列
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # 处理非边界情况
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][columns - 1]


s = Solution()
print(s.minPathSum(grid=[[1, 2, 3], [4, 5, 6]]))
