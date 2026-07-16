class Solution:
    def isPalindrome(self, s: str) -> bool:
        m=""
        for ch in s:
            if ch.isalnum():
                m+=ch.lower()
        if m==m[::-1]:
            return True
        else:
            return False
        
