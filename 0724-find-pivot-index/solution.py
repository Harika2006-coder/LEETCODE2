class Solution(object):
    def pivotIndex(self, nums):
       tsum=sum(nums)
       lsum=0
       rsum=0
       for i,num in enumerate(nums):
        rsum=tsum-lsum-num
        if lsum==rsum:
            return i
        lsum+=num

       return -1        
