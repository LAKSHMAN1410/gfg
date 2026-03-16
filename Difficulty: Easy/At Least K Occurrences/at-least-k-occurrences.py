
class Solution:
    def firstElementKTime(self, arr,k):
        # code here
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            if d[i]==k:
                return i
        return -1            
            
            
    
