class Solution(object):
    def separateDigits(self, nums):
        arr=[]
        for i in nums:
            s=str(i)
            for ch in s:
                arr.append(int(ch))
        return arr
        
