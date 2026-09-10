# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # init current node representatives
        curr1 = list1
        curr2 = list2
        # init vars
        newHead = None
        newCurr = None
        minVal = None
        
        # loop till no nodes left for both
        while curr1 or curr2:
            # check if curr1 and curr2 still have nodes
            if not curr1:
                minVal = curr2.val
                curr2 = curr2.next 
            elif not curr2:
                minVal = curr1.val
                curr1 = curr1.next
            # minVal is from list2 if list1's current node is bigger
            elif curr1.val > curr2.val:
                minVal = curr2.val
                curr2 = curr2.next  
            # minVal is from list1 if list2's current node is equal or bigger
            elif curr2.val >= curr1.val:
                minVal = curr1.val
                curr1 = curr1.next
            
            # if first node in new list, init and use newCurr pointer to build out list, while saving the head separately for return
            if not newHead:
                newCurr = ListNode(minVal)
                newHead = newCurr
            # if not first node, update list via newCurr pointer
            else:
                newCurr.next = ListNode(minVal)
                newCurr = newCurr.next
                        
        return newHead
        