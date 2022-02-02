class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        
        d = {}
        lp = 0
        for i in p:
            d[i] = d.get(i,0)+1
            lp+=1
        
        ls = []
        d2 = {}
        l = 0
        for i in s:
            d2[i] = d2.get(i,0)+1
            ls.append(d2.copy())
            l+=1
        
        
        ans = []
        
        for i in range(l):
            
            start = i
            end = i+lp-1
            
            if end >l-1:
                return ans
            
            if start==0:
                flag=0
                for j in ls[end]:
                    if ls[end][j]==d.get(j,-1):
                        continue
                    else:
                        flag=1
                        break
                #print(ls)
                if flag==0:
                    ans.append(start)
            
            else:
                flag=0
                for j in d:
                    
                    if d[j]==ls[end].get(j,0) - ls[start-1].get(j,0):
                        continue
                    else:
                        flag=1
                        break
                        
                if flag==0:
                    ans.append(start)
                    
            
                    
        return ans            
                    
            
            
            
            
            
            
            
            
        
        
        