"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        # code here
        d={}
        for n in arr:
            if n in d:
                d[n]+=1
            else:
                d[n]=1
        for k,v in d.items():
            if k==x:
                return v 
        return 0        