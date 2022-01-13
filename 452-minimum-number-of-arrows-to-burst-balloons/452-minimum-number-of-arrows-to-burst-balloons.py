class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        
        def fun(x):
            return x[1]
        
        points.sort(key=fun)
        
        n = 0
        l = "0"
        
        
        for i in points:
            
            if l=="0":
                l = i[1]
                n+=1
                continue
            
            if (i[0]<=l)&(i[1]>=l):
                continue
            
            else:
                l = i[1]
                n+=1
                continue
        
        return n
            