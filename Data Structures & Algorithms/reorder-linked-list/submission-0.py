# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nextNode = None
        prev = None 
        curr = head
        
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        midpoint = head
        while fast and fast.next:
            fast = fast.next.next
            midpoint = midpoint.next       
        
        list1 = head
        list2 = self.reverseList(midpoint)
        useTwo = False
        
        node = ListNode()
        head = node
        while list2 and list1:
            if not useTwo:
                node.next = list1
                list1 = list1.next
                useTwo = True
            else:
                node.next = list2
                list2 = list2.next
                useTwo = False
            node = node.next
        
            

            


        



    
        