"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    ans = []
    
    def preorder(self, root: 'Node') -> List[int]:
        self.ans=[]
        def pre(root):
            
            if(root == None):
                return
            self.ans.append(root.val)
            for i in root.children:
                #print(root.val,i.val)
                pre(i)
            return
        pre(root)
        return self.ans
        
        
        
        