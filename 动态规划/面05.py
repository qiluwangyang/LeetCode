"""
给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。

示例 1：
输入: num = 1775(110111011112)
输出: 8

示例 2：
输入: num = 7(01112)
输出: 4
"""


class Solution(object):
    def reverseBits(self, num):
        """
        动态规划转移方程：
            - 数位为1时：cur + 1， insert + 1
            - 数位为0时：insert = cur + 1， cur = 0
        num     1 1 0 1 1 1 0 1 1 1 1
        cur     1 2 0 1 2 3 0 1 2 3 4
        insert  1 2 3 4 5 6 4 5 6 7 8
        :type num: int
        :rtype: int
        """
        cur = 0  # 当前连续1的个数
        insert = 0  # 插入1以后连续1的个数
        m = 1  # 保存insert最大值

        # 32位整数，所以循环范围为32
        for i in range(32):
            if num & (1 << i):
                cur += 1
                insert += 1
            else:
                insert = cur + 1
                cur = 0
            # 需要在判断条件外进行比较，否则只能在遇到0时才会修改m的值
            m = max(m, insert)

        return m


s = Solution()
print(s.reverseBits(1775))
