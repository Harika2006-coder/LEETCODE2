class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n=sorted(arr)
        gap=n[1]-n[0]
        for i in range(len(n)-1):
            if n[i+1]-n[i]!=gap:
                return False
        else:
            return True
        
