"""
给你一个字符串数组words ，只返回可以使用在美式键盘同一行的字母打印出来的单词。键盘如下图所示。美式键盘中：第一行由字符"qwertyuiop"组成。
第二行由字符"asdfghjkl"组成。第三行由字符"zxcvbnm"组成。

示例1：
输入：words = ["Hello", "Alaska", "Dad", "Peace"]
输出：["Alaska", "Dad"]

示例2：
输入：words = ["omk"]
输出：[]

示例3：
输入：words = ["adsdf", "sfd"]
输出：["adsdf", "sfd"]
"""


class Solution(object):
    def findWords(self, words):
        """
       哈希表
        :type words: List[str]
        :rtype: List[str]
        """
        d = dict(zip("qwertyuiop" + "asdfghjkl" + "zxcvbnm",
                     [1] * len("qwertyuiop") + [2] * len("asdfghjkl") + [3] * len("zxcvbnm")))
        ans = []
        for word in words:
            res = 0
            for c in word.lower():
                res += d[c]
            tmp = d[word[0].lower()] * len(word)
            if res == tmp:
                ans.append(word)
        return ans


words = ["dad"]
s = Solution()
print(s.findWords(words))
