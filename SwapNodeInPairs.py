# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode):
        if head is None or head.next is None:
            return head
        values = []
        while head:
            values.append(head.val)
            head = head.next
        for i in range(0, len(values), 2):
            if i + 1 < len(values):
                values[i], values[i + 1] = values[i + 1], values[i]
        h = t = None
        for i in values:
            if h is None:
                h = ListNode(i)
                t = h
            else:
                t.next = ListNode(i)
                t = t.next
        return h

