class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        List1=[]
        for num in nums:
            List1.append(num*num)
        List1.sort()
        return List1
        
