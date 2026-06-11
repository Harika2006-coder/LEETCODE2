class Solution(object):
    def search(self, nums, target):
        nums.sort()
        if target in nums:
            return nums.index(target)
        else:
            return -1
