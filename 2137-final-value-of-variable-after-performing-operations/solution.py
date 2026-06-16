class Solution(object):
    def finalValueAfterOperations(self, operations):
        v=0
        for word in operations:
            if word=="X++" or word=="++X":
                v+=1
            elif word=="X--" or word=="--X":
                v-=1
        return v
