"""
给定一个非负索引rowIndex，返回「杨辉三角」的第rowIndex行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例1:
输入: rowIndex = 3
输出: [1, 3, 3, 1]

示例2:
输入: rowIndex = 0
输出: [1]

示例3:
输入: rowIndex = 1
输出: [1, 1]
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 行数为0不需要单独进行判断
        # if rowIndex == 0:
        #     return [[1]]

        res = []
        # 行数循环仍从0开始
        for i in range(rowIndex + 1):
            tmp = []
            for j in range(i + 1):
                if i == 0 or j == 0 or i == j:
                    tmp.append(1)
                else:
                    tmp.append(res[i - 1][j] + res[i - 1][j - 1])
            res.append(tmp)

        return res[rowIndex]


s = Solution()
print(s.getRow(0))
