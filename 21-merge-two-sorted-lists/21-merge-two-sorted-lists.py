# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
    
        temp = list1
        temp2 = list2
        temp3 = head
    
        while(1):
        
            if(temp==None)&(temp2==None):
                break
            elif(temp==None):
                temp3.next = temp2
                temp2 = None
                continue
            elif(temp2==None):
                temp3.next = temp
                temp=None
                continue
            else:
            
                if(temp.val<=temp2.val):
                
                    temp3.next = temp
                    temp3 = temp3.next
                    temp = temp.next
                    continue
                else:
                    temp3.next = temp2
                    temp3 = temp3.next
                    temp2 = temp2.next
                    continue
    
        return head.next
                
            
            
            