class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        
        d = {}
        point = head
        
        if(head==None):
            return None
        
        # crearing only mapping
        while(point!=None):
            new_node = Node(point.val)
            d[point] = new_node
            point = point.next        
        
        # creating links
        point = head
        
        while(point!=None):
            
            if(point.next!=None):
                d[point].next = d[point.next]
            if(point.random!=None):
                d[point].random = d[point.random]
                
            point = point.next
        
        return d[head]