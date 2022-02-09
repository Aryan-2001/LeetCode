class Solution(object):
    def findPairs(self, nums, k): #O(nlogn)
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort() #O(nlogn)
        
        
        d = {}
        
        for i in nums: #O(n)
            d[i] = d.get(i,0)+1
            
        
        
        
        np = 0
        
        if k==0: #O(n)
            for i in d:
                if d[i]>1:
                    np+=1
            return np
        
        for i in d: #O(n)
            
            if d.get(i+k,0):
                np+=1
        
        return np