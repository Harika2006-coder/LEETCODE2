class Solution(object):
    def pivotInteger(self, n):
        y=n*(n+1)/2
        x=int(math.sqrt(y))
        if x*x==int(y):
            return x
        else:
            return -1
        
