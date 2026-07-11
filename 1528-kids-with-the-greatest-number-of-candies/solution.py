class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        list1=[]
        for i in candies:
            if i+extraCandies <m:
                list1.append(False)
            else:
                list1.append(True)
        return list1
        
