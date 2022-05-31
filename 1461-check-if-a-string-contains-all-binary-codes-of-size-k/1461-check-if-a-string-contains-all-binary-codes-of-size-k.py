class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        
        
        win = s[0:k]
        d = {}
        d[win] = 1
        tot = 1
        for i in s[k:]:
            #print(win)
            win = win[1:]+i
            d[win] = d.get(win,0)+1
            if(d[win]==1):
                tot+=1
        
        if(2**k==tot):
            return True
        else:
            return False
        