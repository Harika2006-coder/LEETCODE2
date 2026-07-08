class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odds=(high-low)//2
        if low%2!=0 or high%2!=0:
            odds+=1
        return odds
