"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        f(0, 0) = 1
        边界值第0行和第0列只有一种移动方式，所以初始化时值为1.
        动态转移函数: f(i, j) = f(i-1, j) + f(j-1)
        :type m: int
        :type n: int
        :rtype: int
        """
        # 初始化二维数组第0行和第0列为1，其他元素为0
        res = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                # 动态转移函数
                res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[m - 1][n - 1]  # 终点为[m-1][n-1]


s = Solution()
print(s.uniquePaths(3, 2))
