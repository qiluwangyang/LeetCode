"""
给你两个整数x和y ，表示你在一个笛卡尔坐标系下的(x, y)处。同时，在同一个坐标系下给你一个数组points ，其中points[i] = [ai, bi]
表示在(ai, bi)处有一个点。当一个点与你所在的位置有相同的x坐标或者相同的y坐标时，我们称这个点是有效的 。
请返回距离你当前位置曼哈顿距离最近的有效点的下标（下标从0开始）。如果有多个最近的有效点，请返回下标
最小的一个。如果没有有效点，请返回 - 1 。

两个点(x1, y1)和(x2, y2)之间的曼哈顿距离为abs(x1 - x2) + abs(y1 - y2) 。

示例1：
输入：x = 3, y = 4, points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
输出：2
解释：所有点中，[3, 1]，[2, 4]和[4, 4]是有效点。有效点中，[2, 4]和[4, 4]距离你当前位置的曼哈顿距离最小，都为1 。[2, 4]的下标最小，所以
返回2 。

示例2：
输入：x = 3, y = 4, points = [[3, 4]]
输出：0
提示：答案可以与你当前所在位置坐标相同。

示例3：
输入：x = 3, y = 4, points = [[2, 3]]
输出：-1
解释：没有有效点。
"""


class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        idx = -1
        distance = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                tmp = abs(x - points[i][0]) + abs(y - points[i][1])
                if distance == -1 or distance > tmp:
                    distance = tmp
                    idx = i

        return idx

    def nearestValidPoint2(self, x, y, points):
        """
        哈希表 + 倒叙遍历
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        d = {}
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                distance = abs(x - points[i][0]) + abs(y - points[i][1])
                if distance in d:
                    d[distance] = d[distance] if d[distance] < i else i
                else:
                    d[distance] = i

        if not d:
            return -1
        return d[min(d.keys())]


x = 5
y = 1
points = [[1, 1], [6, 2], [1, 5], [3, 1]]

s = Solution()
print(s.nearestValidPoint2(x, y, points))
