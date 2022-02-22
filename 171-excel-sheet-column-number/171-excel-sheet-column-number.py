class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        tot = 0
        
        for i in columnTitle:
            
            tot = tot*26 + (ord(i)-ord("A")+1)
        
        return tot
        