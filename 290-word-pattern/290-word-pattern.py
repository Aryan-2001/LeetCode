class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        
        
        ls = s.split()
        lpattern = list(pattern)
        
        if len(ls)!=len(lpattern):
            return False
        
        
        j = 0
        
        d = {}
        d2 = {}
        
        for i in range(len(lpattern)):
            
            key = lpattern[i]
            val = ls[j]
            
            if d.get(key,0)==0:
                d[key] = val
                j+=1
            elif d.get(key,0)==val:
                j+=1
            else:
                return False
            
            if d2.get(val,0)==0:
                d2[val]=key
            elif d2[val]==key:
                continue
            else:
                return False
            
            
        
        
        return True
                
            
            
            