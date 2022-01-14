class Solution:
    def myAtoi(self, s: str) -> int:
        
        
        s = s.strip()
        if s=="":
            return 0
        s = list(s)
        flag = 1 # positive
        
        if s[0]=="+":
            s.pop(0)
            pass
        elif s[0] == "-":
            s.pop(0)
            flag = -1
            pass
        else:
            pass
        
        num = 0
        for i in s:
            
            if (i>="0")&(i<="9"):
                num = num*10 + int(i)
            else:
                break
        
        num = flag*num
        
        if num < -2**31:
            return(-2**31)
        elif num > 2**31-1:
            return(2**31-1)
        else:
            return num 