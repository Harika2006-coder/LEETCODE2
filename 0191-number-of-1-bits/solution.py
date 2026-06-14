class Solution:
    def hammingWeight(self, n: int) -> int:
        b=bin(n)
        s=str(b)
        c=0
        for ch in s:
            if ch == "1":
                c+=1
        return c
        
