class Solution(object):
    def majorityElement(self, nums):
        res=[]
        n=len(nums)
        freq=dict()
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        t=n//3
        for(k,v) in freq.items():
            if v>t:
                res.append(k)
        return res        
