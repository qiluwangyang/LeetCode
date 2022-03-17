class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count_one = sum([1 for i in range(32) if n & (1 << i)])
        return count_one


s = Solution()
print(s.hammingWeight(0b00000000000000000000000000001011))
