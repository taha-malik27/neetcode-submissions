# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev
    

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = self.reverse(head)
        
        curr = head
        count = 1
        while curr:
            if count == n:
                head = curr.next
                break
            
            if (count + 1) == n:
                curr.next = curr.next.next
                break
            
            curr = curr.next
            count += 1
    
        head = self.reverse(head)

        return head





