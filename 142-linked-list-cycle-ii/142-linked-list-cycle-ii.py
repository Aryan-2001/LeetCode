# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        pos = 0
        
        temp = head
        temp2 = None
        while(temp!=None):
            
            if isinstance(temp.val,str):
                flag = 1
                temp2 = temp
                break
            
            temp.val = str(temp.val)
            temp = temp.next
            
        
        if temp2==None:
            return None
        
        else:
            
            temp = head
            while(isinstance(temp.val,str)):
                temp.val = int(temp.val)
                temp = temp.next
            
            return temp2
        