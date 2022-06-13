

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        
        
        ## we will solve this using dp
        
        # triangle can be thought of as a half filled matrix
        rows = len(triangle)
        cols = len(triangle[-1])
        
        dp =  []
        for i in range(rows):
            dp.append([])
            for j in range(cols):
                dp[-1].append(0)
        
        for i in range(rows):
            for j in range(i+1):
                
                if(i==0)&(j==0):
                    dp[i][j] = triangle[i][j]
                elif j==0:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
                elif i==j:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j],dp[i-1][j-1])
        
        return min(dp[rows-1])
                
                
        