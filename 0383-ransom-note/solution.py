class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote_list=list(ransomNote)
        magazine_list=list(magazine) 
        result=[]
        for ch in ransomNote:
            if ch in magazine_list:
                magazine_list.remove(ch)
                result.append(ch)
        if len(result)==len(ransomNote):
                return True
        else:
                return False
