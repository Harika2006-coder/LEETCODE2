class Solution(object):
    def climbStairs(self, n):
        one,two=1,1
        for i in range(n):
            one,two=two,one+two
        return one
        
