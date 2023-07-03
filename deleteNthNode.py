# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        size = 0
        while temp:
            temp = temp.next
            size += 1

        n = size - n + 1
        prev = None
        curr = head
        for i in range(n - 1):
            prev = curr
            curr = curr.next
        if not prev:
            return curr.next
        prev.next = curr.next

        return head