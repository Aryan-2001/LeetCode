class Solution:
    def canPlaceFlowers(self, flower: List[int], n: int) -> bool:
        
        
        l = len(flower)
        if n==0:
            return True
        if n>l:
            return True
        
        if l==1:
            if flower[0]==0:
                return True
            else:
                return False
        
        if(flower[0]==0)&(flower[1]==0):
            flower[0]=1
            n-=1
        
        if n==0:
            return True
        
        for i in range(1,l-1):
            
            if(flower[i]==0)&(flower[i-1]==0)&(flower[i+1]==0):
                n-=1
                flower[i] = 1
                if n==0:
                    return True
        
        if(flower[l-1]==0)&(flower[l-2]==0):
            n-=1
            flower[l-1]=1
            if n==0:
                return True
            
        
        return False
        