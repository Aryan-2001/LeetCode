class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        
        lsl = []
        lsr = []
        
        l = 10**6
        n = len(seats)
        
        for i in seats:
            if i!=1:
                lsl.append(l)
                l+=1
            else:
                lsl.append(0)
                l=1
        l = 10**6
        
        for i in seats[::-1]:
            if i!=1:
                lsr.append(l)
                l+=1
            else:
                lsr.append(0)
                l=1
        #print(lsl)
        #print(lsr)
        
        mx = 0
        for i in range(n):
            mx = max(mx,min(lsl[i],lsr[n-1-i]))
        
        return mx
                
            