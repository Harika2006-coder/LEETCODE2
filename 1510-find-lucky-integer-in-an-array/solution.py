class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic={}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        lucky_max=-1
        for i ,count in dic.items():
            if i==count:
                if i>lucky_max:
                    lucky_max=i
        return lucky_max

        
