"""
在MATLAB中，有一个非常有用的函数reshape ，它可以将一个m x n矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。
给你一个由二维数组mat表示的m x n矩阵，以及两个正整数r和c ，分别表示想要的重构的矩阵的行数和列数。
重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。

如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

示例1：
输入：mat = [[1, 2], [3, 4]], r = 1, c = 4
输出：[[1, 2, 3, 4]]

示例2：
输入：mat = [[1, 2], [3, 4]], r = 2, c = 4
输出：[[1, 2], [3, 4]]
"""


class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        傻瓜式解法
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        l = 0
        tmp = []
        for i in mat:
            l += len(i)
            tmp.extend(i)

        if l != r * c:
            return mat

        res = []
        idx = 0
        for i in range(r):
            # col_list需要在每次行循环开始前清空
            col_list = []
            for j in range(c):
                col_list.append(tmp[idx])
                idx += 1
            res.append(col_list)
        return res

    def matrixReshape2(self, mat, r, c):
        """
        更优雅的代码
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        ans = [[0] * c for _ in range(r)]
        for x in range(m * n):
            # (i, j) -> i * n + j
            # i = x // n
            # j = x % n
            ans[x // c][x % c] = mat[x // n][x % n]

        return ans


mat = [[1, 2], [3, 4]]
r = 4
c = 1

s = Solution()
print(s.matrixReshape(mat, r, c))
