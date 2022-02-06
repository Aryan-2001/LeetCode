class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        prev = None
        
        l = len(nums)
        
        temp = 0
        flag = 0
        for i in range(l):
            
            
            if prev==None:
                
                nums[temp] = nums[i]
                prev = nums[i]
                temp+=1
                flag=1
            
            elif nums[i] == prev:
                if flag==1:
                    nums[temp] =nums[i]
                    temp+=1
                    flag+=1
                else:
                    continue
            
            else:
                nums[temp] = nums[i]
                prev = nums[i]
                temp+=1
                flag=1
        
        return temp
                    
        