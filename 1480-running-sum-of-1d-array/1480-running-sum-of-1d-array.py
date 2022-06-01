class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if(nums==[]):
            return []
        
        ls = []
        ls.append(nums[0])
        for i in nums[1:]:
            ls.append(ls[-1]+i)
        
        return ls
            