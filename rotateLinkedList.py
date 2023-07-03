# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        temp = head
        size = 0
        while temp:
            temp = temp.next
            size += 1

        n = k % size  
        if n == 0 or n == size:
            return head 
        for i in range(n):
            prev = None
            curr = head

            while curr.next:
                prev = curr
                curr = curr.next
            
            prev.next = None
            curr.next = head
            head = curr

        return head