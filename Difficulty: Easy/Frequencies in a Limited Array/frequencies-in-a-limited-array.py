from collections import Counter
class Solution:
    def frequencyCount(self, arr):
        #  code here
        d=Counter(arr)
        arrs=[]
        n=len(arr)
        for i in range(1,n+1):
            if i in d:
                arrs.append(d[i])
            else:
                arrs.append(0)
        return arrs        
                
            
            
            
