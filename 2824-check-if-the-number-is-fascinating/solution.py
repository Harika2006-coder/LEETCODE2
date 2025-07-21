class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n)+str(2*n)+str(3*n)
        return sorted(s) == list("123456789")

        


        
