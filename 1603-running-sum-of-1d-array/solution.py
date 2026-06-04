class Solution(object):
    def runningSum(self, nums):
        res=[]
        s=0
        for num in nums:
            s=s+num
            res.append(s)
        return res
        
