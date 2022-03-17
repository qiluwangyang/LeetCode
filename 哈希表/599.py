"""
假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。

示例 1:
输入: list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["Piatti", "The Grill at Torrey Pines",
 "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”。
"""


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        哈希表
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        min_index_sum = 2 ** 32
        ans = []

        for i in range(len(list1)):
            if list1[i] not in d:
                d[list1[i]] = i

        for j in range(len(list2)):
            if list2[j] in d:
                if min_index_sum > j + d[list2[j]]:
                    min_index_sum = j + d[list2[j]]
                    ans = [list2[j]]
                elif min_index_sum == j + d[list2[j]]:
                    ans.append([list2[j]])

        return ans

    def findRestaurant2(self, list1, list2):
        """
        优雅的写法
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index = {key: value for value, key in enumerate(list1)}
        indexSum = 2 ** 32
        ans = []
        for i in range(len(list2)):
            if list2[i] in index:
                j = index[list2[i]]
                if i + j < indexSum:
                    indexSum = i + j
                    ans = [list2[i]]
                elif i + j == indexSum:
                    ans.append(list2[i])
        return ans


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

s = Solution()
print(s.findRestaurant2(list1, list2))
