"""
仅仅反转字母
给你一个字符串s ，根据下述规则反转字符串：
   所有非英文字母保留在原有位置。
   所有英文字母（小写或大写）位置反转。
返回反转后的s。

示例1：
输入：s = 'ab-cd'
输出：'dc-ba'

示例2：
输入：s = 'a-bC-dEf-ghIj'
输出:'j-Ih-gfE-dCba'

示例3：
输入：s = 'Test1ng-Leet=code-Q!'
输出：'Qedo1ct-eeLg=ntse-T!'
"""


class Solution:
    @staticmethod
    def reverseOnlyLetters1(s: str) -> str:
        """
        使用栈的方式将字符串中所有的字符先传入到列表，在遍历字符串，每遇到一个字符就在res中加入tmp列表的最后一个元素，否则加入非字符元素。
        :param s:
        :return:
        """
        tmp = []
        for i in s:
            if i.isalpha():
                tmp.append(i)

        res = ""
        for i in s:
            if i.isalpha():
                res += tmp.pop()
            else:
                res += i

        return res

    def reverseOnlyLetters2(self, s: str) -> str:
        """
        使用双指针方式遍历字符串，当头指针和尾指针都为字符且头指针小于尾指针时，两个元素交换位置。
        :param s:
        :return:
        """
        # 参数s为字符串，首先需要转换为列表
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            # 左指针指向非字母元素时移动指针
            while left < right and (not s[left].isalpha()):
                left += 1

            # 右指针指向非字母元素时移动指针
            while right >= left and (not s[right].isalpha()):
                right -= 1

            if left < right:
                s[left], s[right] = s[right], s[left]

            # 当两个指针指向的字符都为字母时，指针不会移动，所以需要在此处同时移动两个指针
            left, right = left + 1, right - 1
        return ''.join(s)
