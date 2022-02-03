class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        
        
        d1 = {}
        d2 = {}
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                
                x = nums1[i] + nums2[j]
                y = nums3[i] + nums4[j]
                
                
                d1[x] = d1.get(x,0)+1
                d2[y] = d2.get(y,0)+1
                
        
        tot = 0
        
        for i in d1:
            
            tot+= d1[i] * d2.get(-i,0)
            
        return tot
            
            