class Solution:
    def tribonacci(self, n: int) -> int:
        
        
        if n==1:
            return 1
        
        if n==2:
            return 1
        
        if n==0:
            return 0
        
        ls =[0,1,1]
        
        for i in range(n-2):
            ls.append(ls[-1]+ls[-2]+ls[-3])
            
        return ls[-1]
        