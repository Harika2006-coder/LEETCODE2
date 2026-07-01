class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k=3
        n=len(s)
        l=0
        ans=0
        dici={}
        for r in range(n):
            if s[r] in dici:
                dici[s[r]]+=1
            else:
                dici[s[r]]=1
            if(r-l==k):
                dici[s[l]]-=1
                if dici[s[l]]==0:
                    dici.pop(s[l])
                l+=1
            if len(dici)==k:
                ans+=1
        return ans


        
