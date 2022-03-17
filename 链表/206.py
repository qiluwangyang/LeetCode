"""
给你单链表的头节点head ，请你反转链表，并返回反转后的链表。

示例1：
输入：head = [1, 2, 3, 4, 5]
输出：[5, 4, 3, 2, 1]

示例2：
输入：head = [1, 2]
输出：[2, 1]

示例3：
输入：head = []
输出：[]
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = head  # 将head指向的链表赋值给p1
        p2 = None  # p2用来存放反转的链表

        # 遍历p1，只要p1指向不为None继续循环
        while p1:
            tmp = p1.next  # 存放p1的下一个指向元素
            p1.next = p2  # 断开p1的指向元素，让p1指向p2
            p2 = p1  # p2指向下一个元素
            p1 = tmp  # p1指向下一个元素
        
        return p2
