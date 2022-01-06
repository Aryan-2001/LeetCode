class Solution:
    def fib(self, n: int) -> int:
        
        
        if n==1:
            return 1
        
        if n==0:
            return 0
        
        ls = [0,1]
        
        for i in range(n-1):
            ls.append(ls[-1]+ls[-2])
        
        return ls[-1]