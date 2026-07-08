class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        list1=[]
        for i in nums:
            m=str(i)
            n=0
            for ch in m:
                n+=1
            if n%2==0:
                list1.append(i)
        return len(list1)

            

        
