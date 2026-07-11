class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums=[]
        nums2_copy=list(nums2)
        for i in nums1:
            if i in nums2_copy:
                nums.append(i)
                nums2_copy.remove(i)
        return nums
