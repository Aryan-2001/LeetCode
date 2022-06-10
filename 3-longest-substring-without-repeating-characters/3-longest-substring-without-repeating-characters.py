class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        win = []
        d = {}
        
        mx = 0
        l = 0
        
        for i in s:
            
            if(d.get(i,0)==0):
                
                d[i]  = 1
                win.append(i)
                l+=1
                mx = max(mx,l)
            
            else:
                
                x = win.pop(0)
                l-=1
                d[x]-=1
                while(x!=i):
                    x = win.pop(0)
                    l-=1
                    d[x]-=1
                win.append(i)
                l+=1
                d[i]+=1
                mx = max(mx,l)
        
        return mx
                    
                    
                
        
        