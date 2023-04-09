# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    nodes = []
    track = head
    while track:
        nodes.append(track)
        track = track.next
    if n == len(nodes):
        head = head.next
    elif n == 1:
        nodes[-2].next = None
        nodes[-1] = None
    else:
        nodes[-n-1].next = nodes[-n+1]
        nodes[-n] = None
    return head