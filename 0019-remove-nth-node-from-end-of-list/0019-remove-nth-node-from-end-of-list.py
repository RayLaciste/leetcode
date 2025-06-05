# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0, head) # `dummy` Node preppended to List
        left = d # index 0
        right = head # index 1

        while n > 0 and right: # pointing to where the item we want to remove
            right = right.next
            n -= 1 
        
        while right: # while right is not None, move pointers
            left = left.next
            right = right.next

        # delete - next is next.next ( skipping the node `next`)
        left.next = left.next.next
        return d.next # returns all nodes after d (index 0)