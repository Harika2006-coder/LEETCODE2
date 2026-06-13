class Solution(object):
    def canBeEqual(self, target, arr):
        return True if sorted(target)==sorted(arr) else False
