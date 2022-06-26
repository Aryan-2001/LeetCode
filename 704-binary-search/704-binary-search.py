class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        l = 0
        r = len(nums)-1
        
        if(r==-1):
            return -1
        
            
        
        mid = int((l+r)/2)
        
        while(l<r):
            
            if(l==r-1):
                if(nums[l]==target):
                    return l
                elif(nums[r]==target):
                    return r
                else:
                    return -1
            
            if(nums[mid]<target):
                l = mid
                mid = int((l+r)/2)
                continue
            
            elif(nums[mid]>target):
                r = mid
                mid = int((l+r)/2)
                continue
                
            elif (nums[mid]==target):
                return mid
            
        if(nums[mid]==target):
            return mid
        else:
            return -1
            
            
        
        