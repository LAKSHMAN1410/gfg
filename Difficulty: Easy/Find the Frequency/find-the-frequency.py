"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
from collections import Counter
class Solution:
    def findFrequency(self, arr, x):
        # code here
        d=Counter(arr)
        for k,v in d.items():
            if k==x:
                return v 
        return 0        