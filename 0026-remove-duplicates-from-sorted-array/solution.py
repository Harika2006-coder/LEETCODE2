class Solution(object):
    def removeDuplicates(self, nums):
       nums.sort()
       arr=[]
       arr1=[]
       for num in nums:
        if num in arr:
            arr1.append("_")
        else:
            arr.append(num)
       arr2= arr + arr1
       nums[:]= arr2
       return len(arr)

        
