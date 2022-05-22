class Solution:
    def countSubstrings(self, s: str) -> int:
        
        
        
        n = len(s)
        
        dp = []
        for i in range(n):
            dp.append([])
            for j in range(n):
                dp[-1].append(0)
        
        
        # for one length sub strings always palindromic
        for i in range(n):
            dp[i][i] = 1
            
        tot = 0
        for t in range(n):
            for i in range(n):
                
                j = i+t
                
                if j>=n:
                    break
                
                if i==j:
                    tot+=1
                    continue
                
                if s[i]!=s[j]:
                    continue
                
                if s[i]==s[j]:
                    if(i+1==j):
                        dp[i][j]=1
                        tot+=1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                        if(dp[i][j]):
                            tot+=1
        print(dp)
        return tot
                        
                    
            
        