class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        l = len(cost)
        
        ls = []
        
        for i in range(l+1):
            ls.append(100000)
            
            
        for i in range(l+1):
            
            if i==0:
                ls[i] = 0
                continue
            if i==1:
                ls[i] = 0
                continue
                
            else:
                ls[i] = min(ls[i-1]+cost[i-1] , ls[i-2]+cost[i-2])
                
        #print(ls)
                
        return ls[l]
        