class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        row = len(matrix)
        col = len(matrix[0])
        
        ans = []
        
        for i in range(col):
            ans.append([])
            for j in range(row):
                ans[-1].append(0)
                
        for i in range(row):
            for j in range(col):
                
                ans[j][i] = matrix[i][j]
        
        return ans