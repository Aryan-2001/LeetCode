# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        
        if(n==1):
            return 1
        
        
        l = 0
        r = n
        d = {}
        while(l<r):
            #print(d)
            mid = int((l+r)/2)
            
            if(l==r-1):
                if(isBadVersion(l)==False)&(isBadVersion(r)==True):
                    return r
            
            y = isBadVersion(mid)
            d[mid] = y
            
            if(y==False):
                l = mid
                mid = int((l+r)/2)
                continue
            
            else:
                if(d.get(mid-1,0)==0):
                    d[mid-1] = isBadVersion(mid-1)
                    
                if(d[mid-1]==True):
                    r = mid
                    mid = int((l+r)/2)
                    continue
                else:
                    return mid
                
                
                
                
                
                
                
                
                
                
            
            
        