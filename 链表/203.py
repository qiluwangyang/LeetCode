"""
给你一个链表的头节点head和一个整数val ，请你删除链表中所有满足Node.val == val的节点，并返回新的头节点 。

示例1：
输入：head = [1, 2, 6, 3, 4, 5, 6], val = 6
输出：[1, 2, 3, 4, 5]

示例2：
输入：head = [], val = 1
输出：[]

示例3：
输入：head = [7, 7, 7, 7], val = 7
输出：[]
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pass
