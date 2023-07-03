# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        temp_list = ListNode(0, head)
        prev = temp_list

        for i in range(left - 1):
            prev = prev.next
        
        curr = prev.next
        next = None

        for i in range(right - left):
            next = curr.next

            curr.next = next.next
            next.next = prev.next
            prev.next = next
        
        return temp_list.next


        