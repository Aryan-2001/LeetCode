class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if nums == []:
            return [[]]
        
        x = nums.pop()
        
        ls = self.subsets(nums)
        
        lt = []
        #print(x,nums,ls)
        for i in ls:
            lt.append(i.copy())
            i.append(x)
            
        ls = ls+lt
        return ls