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
        prev = None
        while curr:
            if count == n:
                if not prev:
                    head = curr.next
                else:
                    prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            count += 1
    
        head = self.reverse(head)

        return head





