from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode()
    track = head
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            track.next = list1
            list1 = list1.next
        else:
            track.next = list2
            list2 = list2.next
        track = track.next
    while list1 is not None:
        track.next = list1
        list1 = list1.next
        track = track.next
    while list2 is not None:
        track.next = list2
        list2 = list2.next
        track = track.next
    head = head.next
    return head


class Solution:
    pass
