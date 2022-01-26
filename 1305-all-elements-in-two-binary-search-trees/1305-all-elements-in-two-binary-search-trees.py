# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        
        
        def return_sorted(root):
            
            if root == None:
                return []
            
            return return_sorted(root.left) + [root.val] + return_sorted(root.right)
        
        
        x = return_sorted(root1)
        y = return_sorted(root2)
        
        #print(x,y)
        
        l = len(x)
        l2 = len(y)
        
        ans = []
        
        i = 0
        j = 0
        
        while(1):
            
            if(i==l)&(j==l2):
                break
            
            if i==l:
                ans += y[j:]
                break
            
            if j==l2:
                ans += x[i:]
                break
                
            
            if x[i] == y[j]:
                ans.append(x[i])
                ans.append(y[j])
                i+=1
                j+=1
                continue
            
            if x[i] < y[j]:
                ans.append(x[i])
                i+=1
                continue
            
            if y[j] < x[i]:
                ans.append(y[j])
                j+=1
                continue
                
        return ans
                
            
            
            
            
            
        