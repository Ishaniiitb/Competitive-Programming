# https://leetcode.com/problems/remove-linked-list-elements/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def removeElements(head: ListNode, val):
    while head is not None and head.val == val:
        head = head.next
    if head:
        track = head
        while track is not None and track.next is not None:
            if track.next.val == val:
                temp = track.next
                track.next = temp.next
                temp = None
                continue
            track = track.next
    return head
