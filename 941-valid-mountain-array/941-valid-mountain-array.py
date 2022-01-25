class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        
        flag = 1 # in the start 1 for strictly increasing and -1 for strictly decreasing
        
        prev = arr[0]
        inc = 0
        dec= 0 
        for i in arr[1:]:
            
            if flag==1:
                
                if i > prev:
                    inc+=1
                    prev = i
                    continue
                elif i==prev:
                    return False
                else:
                    if inc==0:
                        return False
                    else:
                        prev = i
                        dec+=1
                        flag = -1
                        continue
            
            else:
                
                if i < prev :
                    dec+=1
                    prev = i
                    continue
                
                else:
                    return False
        
        if(inc==0)|(dec==0)|(flag!=-1):
            return False
        else:
            return True
                
            
        
        