# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next: # to get the middle of the list
            slow = slow.next # find where slow ends up
            fast = fast.next.next # fast moves twice as fast as slow
        
        # reverse the second half
        second = slow.next
        prev = slow.next = None # prev is slow.next (head of the second half) THEN the next of slow, is null
        while second: # while second is not null, swap 
            tmp = second.next 
            second.next = prev
            prev = second
            second = tmp
        
        # merge halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2