class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a=dividend/divisor
        if a>2147483647:
            return 2147483647
        return int(a)
        
