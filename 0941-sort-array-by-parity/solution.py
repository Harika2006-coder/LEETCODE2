class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        List1=[]
        List2=[]
        for i in nums:
            if i%2==0:
                List1.append(i)
            else:
                List2.append(i)
        
        List3=List1+List2
        return List3

        
