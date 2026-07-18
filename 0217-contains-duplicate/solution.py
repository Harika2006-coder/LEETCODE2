class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        s=set(nums)
        if n==len(s):
            return False
        else:
            return True
        
