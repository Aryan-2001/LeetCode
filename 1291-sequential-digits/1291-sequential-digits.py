class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        
        nd1 = len(str(low))
        nd2 = len(str(high))
        
        
        ls = []
        num2 = 0
        unit = 1
        
        for i in range(nd1):
            ls.append(str(unit))
            unit+=1
            num2 = 10*num2+1
            if unit==10:
                return []
        
        num = int("".join(ls))
        umax = 10 - nd1
        
        unit = 1
        ans = []
        
        temp = num
        td = nd1
        temp2 = num2
        while(1):
            
            if(temp<low):
                if(int(str(temp)[0])==umax):
                    umax-=1
                    temp = num*10+ td +1
                    td+=1
                    num = temp
                    temp2 = temp2*10+1
                    continue
                else:
                    temp = temp+temp2
                    continue
            
            elif(temp>high):
                break
            else:
                ans.append(temp)
                if(int(str(temp)[0])==umax):
                    umax-=1
                    temp = num*10+ td +1
                    td+=1
                    num = temp
                    temp2 = temp2*10+1
                    continue
                else:
                    temp = temp+temp2
                    continue
        
        return ans
                
                
                
                    
                
        