class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list1=nums[0:n]
        list2=nums[n:]
        nums1=[]
        for i in range(n):
            nums1.append(list1[i])
            nums1.append(list2[i])
        return nums1
        
