class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        d = {}
        
        temp1 = 0
        temp2 = 0
        index = 0
        
        while(1):
            
            if(temp1==m)&(temp2==n):
                break
            
            elif(temp1==m):
                
                d[index] = nums2[temp2]
                temp2+=1
                index+=1
            
            elif(temp2==n):
                d[index] = nums1[temp1]
                temp1+=1
                index+=1
            
            elif(nums1[temp1]<=nums2[temp2]):
                d[index] = nums1[temp1]
                temp1+=1
                index+=1
            
            else:
                d[index] = nums2[temp2]
                temp2+=1
                index+=1
        
        for i in d:
            nums1[i] = d[i]
            
            
            
            