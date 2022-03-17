"""
给你一个整数数组salary ，数组里每个数都是唯一的，其中salary[i]是第i个员工的工资。
请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。

示例1：
输入：salary = [4000, 3000, 1000, 2000]
输出：2500.00000
解释：最低工资和最高工资分别是1000和4000 。去掉最低工资和最高工资以后的平均工资是(2000 + 3000) / 2 = 2500

示例2：
输入：salary = [1000, 2000, 3000]
输出：2000.00000
解释：最低工资和最高工资分别是1000和3000 。去掉最低工资和最高工资以后的平均工资是(2000) / 1 = 2000

示例3：
输入：salary = [6000, 5000, 4000, 3000, 2000, 1000]
输出：3500.00000

示例4：
输入：salary = [8000, 9000, 2000, 3000, 6000, 1000]
输出：4750.00000
"""


class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        min_salary = max_salary = salary[0]
        sum_salary = 0
        for s in salary:
            if min_salary > s:
                min_salary = s
            if max_salary < s:
                max_salary = s
            sum_salary += s

        return (sum_salary - min_salary - max_salary) / (len(salary) - 2)


salary = [48000, 59000, 99000, 13000, 78000, 45000, 31000, 17000, 39000, 37000, 93000, 77000, 33000, 28000, 4000, 54000,
          67000, 6000, 1000, 11000]
s = Solution()
print(s.average(salary))
