class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n=[]
        p=""
        for chr in s:
            if chr not in p:
                p+=chr
            else:
                n.append(p)
                p=p[p.index(chr)+1:] + chr
        n.append(p)
        length=[len(w) for w in n]
        return max(length) if length else 0
        

        

        
