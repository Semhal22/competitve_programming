# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return head
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        curr = head

        while prev:
            if curr.val != prev.val:
                return False
            curr = curr.next
            prev = prev.next
        
        return True