class Solution:
    def getMinMax(self, arr):
        # code here
        arr=sorted(arr)
        return arr[0],arr[-1]