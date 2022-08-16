class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        d = {}
        
        for i in s:
            d[i] = d.get(i,0)+1
        temp = 0
        for i in s:
            if d[i] == 1:
                return temp
            temp+=1
        
        return -1