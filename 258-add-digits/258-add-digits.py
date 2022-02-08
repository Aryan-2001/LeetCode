class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        s = str(num)
        
        while(len(s)!=1):
            
            tot = 0
            
            for i in s:
                
                tot+=int(i)
                
            s = str(tot)
            
        return int(s)