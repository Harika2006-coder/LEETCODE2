class Solution(object):
    def pivotArray(self, nums, pivot):
        left=[]
        right=[]
        p=[]
        for num in nums:
            if num<pivot:
                left.append(num)
            elif num==pivot:
                p.append(num)
            else:
                right.append(num)
        return left+p+right
        
        
