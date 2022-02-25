class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        
        flag1 = 0
        flag2 = 0
        
        ls = list(map(int,version1.split(".")))
        ls2 = list(map(int,version2.split(".")))
       
        
        while(1):
            
            if ls == []:
                a = 0
            else:
                a = ls.pop(0)
            
            if ls2 == []:
                b = 0
            else:
                b = ls2.pop(0)
                
            if(a>b):
                return 1
            elif(b>a):
                return -1
            elif(ls==[])&(ls2==[])&(a==b):
                return 0
            else:
                continue
            