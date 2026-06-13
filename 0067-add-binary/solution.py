class Solution:
    def addBinary(self, a: str, b: str) -> str:
      decimal_a=int(a,2)
      decimal_b=int(b,2)
      total_sum=decimal_a+decimal_b
      return f"{total_sum:b}"
