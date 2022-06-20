class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        
        ans  = []
        
        sm =  0
        
        for i in nums:
            sm+=i
            ans.append(sm)
            
        return ans