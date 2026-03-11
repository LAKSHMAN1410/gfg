class Solution:
    def search(self, arr, x):
        # code here
        ans=-1
        for i in range(0,len(arr)):
            if x==arr[i]:
                ans=i
                break
        if ans==-1:
            return ans
        else:
            return ans