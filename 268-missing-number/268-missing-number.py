class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        i = len(nums)
        sm = i*(i+1)/2
        
        for i in nums:
            sm-=i
        
        return int(sm)
        