class Solution:
    def search(self, arr, x):
        # code here
        index = -1
        for i in arr:
            if i == x :
                index = arr.index(x)
        
        return index