class Solution:
    def areAnagrams(self, s1, s2):
       # code here
       a=list(s1)
       b=list(s2)
       a.sort()
       b.sort()
       if a==b:
           return True