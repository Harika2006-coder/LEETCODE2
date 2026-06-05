class Solution(object):
    def isHappy(self, n):
        s1=set()
        while n!=1 and n not in s1:
            s1.add(n)
            n=sum(int(d)**2 for d in str(n))
        return n==1
        
