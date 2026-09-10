# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # init vars
        slow = head
        fast = head

        # loop until end of list (if it exists), 
        # cannot have infinite loop as if there is no end and is a cycle, 
        # its guaranteed to be caught and returned
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # if slow == fast at any point, it means fast came back around so cycle
            if slow == fast:
                return True
        
        
        # if break the loop we encountered an end so return False
        return False