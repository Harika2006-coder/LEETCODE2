class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        s1=" "
        s2=" "
        for ch in word1:
            s1+=ch
        for ch in word2:
            s2+=ch
        if s1==s2:
           return True
        else:
            return False
        
