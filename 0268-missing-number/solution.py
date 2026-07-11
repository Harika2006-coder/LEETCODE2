class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m=0
        for i in range(len(nums)+1):
            m+=i
        return m-sum(nums)
       
        
