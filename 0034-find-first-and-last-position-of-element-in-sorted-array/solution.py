class Solution(object):
    def searchRange(self, nums, target):
     arr=[]
    
     for i in range(len(nums)):
        if nums[i]==target :
            arr.append(i)
     if len(arr)>0:
        return [arr[0],arr[-1]]
     else:
        return [-1,-1]
        
