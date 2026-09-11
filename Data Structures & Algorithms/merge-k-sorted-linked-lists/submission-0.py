# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge2Lists(self, l1:Optional[ListNode] , l2:Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        head = node

        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        
        if l1:
            node.next = l1
        else:
            node.next = l2

        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        mid = n//2
        head = None
        if n > 1:
            l1 = self.mergeKLists(lists[:mid])
            l2 = self.mergeKLists(lists[mid:])
            head = self.merge2Lists(l1, l2)
     
        elif n == 1:
            head = lists[0]
        
        return head



