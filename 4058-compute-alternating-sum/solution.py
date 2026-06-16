class Solution(object):
    def alternatingSum(self, nums):
        even,odd=0,0
        for i in range(len(nums)):
            if i%2==0:
               even+=nums[i]
            else:
                odd+=nums[i]
        return even-odd
