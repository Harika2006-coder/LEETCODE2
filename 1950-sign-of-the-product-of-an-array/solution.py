class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign=1
        for i in nums:
           if i==0:
            return 0
           elif i>0:
            continue
           else:
            sign=-1*sign
        return sign
        
