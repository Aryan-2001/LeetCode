# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if(head==None):
            return None
        
        ls = []
        
        temp = head
        l = 0
        while(temp!=None):
            
            ls.append(temp.val)
            temp = temp.next
            l+=1
        
        
        k = k%l
        
        temp = head
        temp2 = 0
        while(temp!=None):
            temp.val = ls[(temp2-k)%l]
            temp2+=1
            temp = temp.next
        
        return head
        