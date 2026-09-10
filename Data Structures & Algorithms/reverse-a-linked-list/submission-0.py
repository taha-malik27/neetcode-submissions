# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
                # hold next value so we dont lose it
                temp = curr.next
                # reverse links
                curr.next = prev
                # update nodes
                prev = curr
                curr = temp
        
        new_head = prev
        return new_head

        
                