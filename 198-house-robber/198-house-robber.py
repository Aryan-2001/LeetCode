class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        ls =[]
        l=0
        
        for i in nums:
            ls.append([0,0])
            l+=1
        
        # 0th index in each ls entry is max value and 1st index is 0,1 with 0 as choosen and 1 not chosen
        
        for i in range(l):
            
            if i==0:
                ls[i] = [nums[i],1]
                continue
            
            if i==1:
                
                if nums[i] > nums[i-1]:
                    ls[i] = [nums[i],1]
                else:
                    ls[i] = [nums[i-1],0]
                continue
            
            else:
                
                if ls[i-1][1] == 0: #if last is not choosen
                    ls[i] = [max(ls[i-1][0],ls[i-2][0])+nums[i] ,1]
                else:
                    
                    if ls[i-1][0] >= ls[i-2][0]+nums[i]:
                        ls[i] = [ls[i-1][0],0]
                    else:
                        ls[i] = [ls[i-2][0]+nums[i],1]
                continue
                        
        return ls[-1][0]
                
            