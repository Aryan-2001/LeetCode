class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        
        mx = 0 
        win = []
        d = {}
        sm = 0
        
        for i in nums:
            
            if(d.get(i,0)==0):
                win.append(i)
                sm+=i
                d[i] = 1
            else:
                
                x = win.pop(0)
                d[x]-=1
                sm-=x
                while(x!=i):
                    x = win.pop(0)
                    d[x]-=1
                    sm-=x
                win.append(i)
                sm+=x
                d[i]+=1
            
            mx = max(mx,sm)
        
        return mx
                
            
        