class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        
        d = {}
        
        for i in s:
            d[i] = d.get(i,0)+1
            
        flag = 0
        length = 0
        
        for i in d:
            
            if(d[i]%2==0):
                length+=d[i]
            else:
                length+=int(d[i]-1)
                flag = 1
        
        length+=flag
        return length