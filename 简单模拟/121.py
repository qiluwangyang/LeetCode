"""
给定一个数组prices ，它的第i个元素prices[i]表示一支给定股票第i天的价格。你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该
股票。设计一个算法来计算你所能获取的最大利润。返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回0。

示例1：
输入：[7, 1, 5, 3, 6, 4]
输出：5
解释：在第2天（股票价格 = 1）的时候买入，在第5天（股票价格 = 6）的时候卖出，最大利润 = 6 - 1 = 5 。
注意利润不能是7 - 1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例2：
输入：prices = [7, 6, 4, 3, 1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为0。
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        暴力解法，超出时间限制
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                max_profit = max_profit if prices[j] - prices[i] < max_profit else prices[j] - prices[i]
        return max_profit

    def maxProfit2(self, prices):
        """
        一次循环
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min_price if min_price < prices[i] else prices[i]
            max_profit = max_profit if max_profit > prices[i] - min_price else prices[i] - min_price
        return max_profit


s = Solution()
print(s.maxProfit2([7, 1, 5, 3, 6, 4]))
