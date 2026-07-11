class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        counts=[]
        for i in sentences:
            c=0
            for sentence in i:
                for ch in sentence:
                    if ch==" ":
                        c+=1
            counts.append(c)
        return max(counts)+1
        
