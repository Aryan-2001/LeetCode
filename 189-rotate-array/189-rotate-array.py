class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        l = len(nums)
        k = k%l
        
        ans =[]
        
        for i in range(l):
            
            ans.append(nums[(i-k)%l])
        
        for i in range(l):
            nums[i] = ans[i]
            
        
        