# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: ListNode, l2: ListNode):
    vals = {10: 0, 11: 1, 12: 2, 13: 3, 14: 4, 15: 5, 16: 6, 17: 7, 18: 8, 19: 9}
    carry = False
    head = tail = None
    while l1 is not None and l2 is not None:
        d = l1.val + l2.val
        if carry:
            d += 1
        if d in vals:
            carry = True
            d = vals[d]
        else:
            carry = False
        if head is None:
            head = ListNode(d)
            tail = head
        else:
            tail.next = ListNode(d)
            tail = tail.next
        l1, l2 = l1.next, l2.next
    while l1 is not None:
        d = l1.val
        if carry:
            d += 1
        if d in vals:
            carry = True
            d = vals[d]
        else:
            carry = False
        tail.next = ListNode(d)
        tail = tail.next
        l1 = l1.next
    while l2 is not None:
        d = l2.val
        if carry:
            d += 1
        if d in vals:
            carry = True
            d = vals[d]
        else:
            carry = False
        tail.next = ListNode(d)
        tail = tail.next
        l2 = l2.next
    if carry:
        tail.next = ListNode(1)
        tail = tail.next
    return head
