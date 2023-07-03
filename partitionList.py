# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        partition_one = ListNode()
        partition_two = ListNode()

        tail_one = partition_one
        tail_two = partition_two

        curr = head
        while curr:
            new_node = ListNode(curr.val)
            if curr.val < x:
                tail_one.next = new_node
                tail_one = tail_one.next
            else:
                tail_two.next = new_node
                tail_two = tail_two.next
            curr = curr.next
        
        tail_one.next = None
        tail_one.next = partition_two.next

        return partition_one.next
        
            
