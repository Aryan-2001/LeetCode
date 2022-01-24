class Solution:
    def detectCapitalUse(self, words: str) -> bool:
        
        
        
        flag = None
        l = len(words)
        if l==1:
            return True
        
        
        if(words[0] >="A")&(words[0]<="Z"):
            flag = 1 # representing all words should be caps or first wird caps and rest lower
        else:
            flag = 0 # representing all words should be lower
            
        
        if flag==0:
            for i in words[1:]:
                if(i>="a")&(i<="z"):
                    continue
                else:
                    return False
            return True
        
        else:
            
            if l==2:
                return True
            else:
                if(words[1] >= "A")&(words[1]<="Z"):
                    flag = 1 # rep all caps
                else:
                    flag = 0 # rep all lower
            
            if flag:
                
                for i in words[2:]:
                    if(i>="A")&(i<="Z"):
                        continue
                    else:
                        return False
                    
                return True
            
            else:
                for i in words[2:]:
                    if(i>="a")&(i<="z"):
                        continue
                    else:
                        return False
                
                return True
            
            