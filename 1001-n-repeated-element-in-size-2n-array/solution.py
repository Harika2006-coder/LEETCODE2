class Solution(object):
    def repeatedNTimes(self, nums):
        mySet=set()
        for i in nums:
            if i in mySet:
                return i
            else:
                mySet.add(i)
