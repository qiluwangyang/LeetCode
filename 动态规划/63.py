"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        错误方法，一直在打补丁
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        for i in range(m):
            for j in range(n):
                if all(obstacleGrid[i]) == 1:
                    return 0

        for i in range(n):
            for j in range(m):
                if all(obstacleGrid[j]) == 1:
                    return 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
                if i == 0 or j == 0:
                    if obstacleGrid[i][j] != -1:
                        obstacleGrid[i][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i - 1][j] == -1:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                elif obstacleGrid[i][j - 1] == -1:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                elif obstacleGrid[i][j] == -1:
                    continue
                else:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]
        if obstacleGrid[m - 1][n - 1] == -1:
            return 0
        return obstacleGrid[m - 1][n - 1]

    def uniquePathsWithObstacles2(self, obstacleGrid):
        """
        降维，将二维数组压缩为一维
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)     # 行
        m = len(obstacleGrid[0])  # 列
        f = [0] * m
        f[0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    f[j] = 0
                    continue

                if j - 1 >= 0 and obstacleGrid[i][j - 1] == 0:
                    f[j] += f[j - 1]
        return f[m - 1]

    def uniquePathsWithObstacles3(self, obstacleGrid):
        """
        动态规划
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)  # 行
        n = len(obstacleGrid[0])  # 列
        dp = [[0] * n for _ in range(m)]
        # 处理起始位置为障碍物
        dp[0][0] = 0 if obstacleGrid[0][0] == 1 else 1

        # 处理第一列有障碍物
        for i in range(1, n):
            if obstacleGrid[0][i] == 1 or dp[0][i - 1] == 0:  # 当第一列中有障碍物时，则障碍物及后面的元素路径都为0
                dp[0][i] = 0
            else:
                dp[0][i] = 1

        # 处理第一行有障碍物
        for j in range(1, m):
            if obstacleGrid[j][0] == 1 or dp[j - 1][0] == 0:  # 当第一行中有障碍物时，则障碍物及后面的元素路径都为0
                dp[j][0] = 0
            else:
                dp[j][0] = 1

        # 处理障碍物在非边界的情况
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:  # 障碍物在非第一行或第一列的情况
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


s = Solution()
print(s.uniquePathsWithObstacles3(obstacleGrid=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
