class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        
        sm = 0 
        
        mt = []
        l = 0
        for i in nums:
            sm+=i
            mt.append(sm)
            l+=1
        
        #print(mt)
        temp = 0
        
        for i in mt:
            
            if(temp==0):
                
                left = 0
                right = mt[-1] - i
            
            elif(temp==l-1):
                
                left = mt[-2]
                right = 0
            
            else:
                
                left = mt[temp-1]
                right = mt[-1] - mt[temp]
                
            temp+=1
            #print(left,right)
            if(left==right):
                return temp-1
            
        return -1
            
            
        