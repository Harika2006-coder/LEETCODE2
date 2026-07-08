class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m=str(n)
        add=0
        product=1
        for ch in m:
            add+=int(ch)
            product*=int(ch)
        return product- add

        
