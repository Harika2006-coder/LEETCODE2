class Solution(object):
    def plusOne(self, digits):
       s=" "
       for num in digits:
        s+=str(num)
       a=int(s)+1
       s1=str(a)
       arr=[]
       for ch in s1:
        arr.append(int(ch))
       return arr

