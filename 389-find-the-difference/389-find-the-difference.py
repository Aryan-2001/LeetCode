class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        
        d = {}
        
        for i in s:
            d[i] = d.get(i,0)+1
        
        
        for i in t:
            
            if d.get(i,0)==0:
                return i
            else:
                d[i]-=1
                continue
                