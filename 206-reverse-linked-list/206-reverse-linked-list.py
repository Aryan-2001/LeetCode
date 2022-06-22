# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if(head==None):
            return None
        def reverse(prev,present):
            present.next = prev
            
            
        prev = None
        present = None
        future = None
        
        temp = head
        while(temp!=None):
            if(prev==None):
                prev = temp
                temp = temp.next
                continue
            
            present = temp
            temp = temp.next
            present.next = prev
            prev = present
            continue
        
        if(present==None):
            return head
        
        head.next = None
        return present
            
            
            
            
            
            
        