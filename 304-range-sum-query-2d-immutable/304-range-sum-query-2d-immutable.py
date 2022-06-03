class NumMatrix(object):

    def __init__(self, matrix):
        
        """:type matrix: List[List[int]]"""
        
        row = len(matrix)
        col = len(matrix[0])
        
        self.ans = []
        
        for i in range(row):
            self.ans.append([])
            for j in range(col):
                self.ans[-1].append(0)
                
        for i in range(row):
            for j in range(col):
                
                if(i==0)&(j==0):
                    self.ans[i][j] = matrix[i][j]
                
                elif i==0:
                    self.ans[i][j] = matrix[i][j]+self.ans[i][j-1]
                    
                elif j==0:
                    self.ans[i][j] = matrix[i][j] + self.ans[i-1][j]
                    
                else:
                    self.ans[i][j] = self.ans[i-1][j] + self.ans[i][j-1] - self.ans[i-1][j-1]+matrix[i][j] 
                    
        print(self.ans)
        

    
    def sumRegion(self, row1, col1, row2, col2):
        """:type row1: int,:type col1: int,:type row2: int,:type col2: int,:rtype: int"""
        
        if(row1==0)&(col1==0):
            return self.ans[row2][col2]
        elif(row1==0):
            return self.ans[row2][col2]-self.ans[row2][col1-1]
        elif(col1==0):
            return self.ans[row2][col2]-self.ans[row1-1][col2]
        else:
            return self.ans[row2][col2] - self.ans[row2][col1-1] - self.ans[row1-1][col2]+self.ans[row1-1][col1-1]
        
        
        
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)