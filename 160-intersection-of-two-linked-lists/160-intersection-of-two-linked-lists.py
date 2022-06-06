# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        
        temp = headA
        
        while(temp!=None):
            temp.val = -1*temp.val
            temp = temp.next
        
        temp = headB
        while(temp!=None):
            if(temp.val>0):
                temp = temp.next
            else:
                break
        
        ## temp is the answer
        
        ## now change back the values ,ututaed
        
        temp2 = headA
        while(temp2!=None):
            temp2.val = -1*temp2.val
            temp2 = temp2.next
        
        return temp
        
        