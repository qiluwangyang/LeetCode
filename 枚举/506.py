"""
给你一个长度为n的整数数组score ，其中score[i]是第i位运动员在比赛中的得分。所有得分都互不相同 。
运动员将根据得分决定名次 ，其中名次第1的运动员得分最高，名次第2的运动员得分第2高，依此类推。运动员的名次决定了他们的获奖情况：
名次第1的运动员获金牌"Gold Medal" 。名次第2的运动员获银牌"Silver Medal" 。名次第3的运动员获铜牌"Bronze Medal" 。从名次第4到第n的运动
员，只能获得他们的名次编号（即，名次第x的运动员获得编号"x"）。使用长度为n的数组answer返回获奖，其中answer[i]是第i位运动员的获奖情况。

示例1：
输入：score = [5, 4, 3, 2, 1]
输出：["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]解释：名次为[1st, 2nd, 3rd, 4th, 5th] 。

示例2：
输入：score = [10, 3, 8, 9, 4]
输出：["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
解释：名次为[1st, 5th, 3rd, 2nd, 4th] 。
"""


class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        d = {}
        ans = []
        tmp = list(score)
        tmp.sort(reverse=True)
        for i in range(len(tmp)):
            if tmp[i] not in d:
                if i == 0:
                    d[tmp[i]] = "Gold Medal"
                elif i == 1:
                    d[tmp[i]] = "Silver Medal"
                elif i == 2:
                    d[tmp[i]] = "Bronze Medal"
                else:
                    d[tmp[i]] = str(i + 1)

        for j in score:
            ans.append(d[j])

        return ans

    def findRelativeRanks2(self, score):
        """
        优雅写法，枚举
        :type score: List[int]
        :rtype: List[str]
        """

        desc = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ans = [""] * len(score)
        arr = sorted(enumerate(score), key=lambda x: x[-1])
        for i, (idx, _) in enumerate(arr):
            ans[idx] = desc[i] if i < 3 else str(i + 1)
        return ans


s = Solution()
print(s.findRelativeRanks2([10, 3, 8, 9, 4]))
