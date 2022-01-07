class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        if n==1:
            return 1
        if n==2:
            return 2
        ls = [1,2]
        
        for i in range(n-2):
            ls.append(ls[-1]+ls[-2])
            
        return ls[-1]