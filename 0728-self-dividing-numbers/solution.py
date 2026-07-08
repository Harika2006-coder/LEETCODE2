class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        list1=[]
        for i in range(left,right+1):
            m=str(i)
            valid =True
            for ch in m:
                p=int(m)
                q=int(ch)
                if q==0 or p%q!=0:
                  valid=False
                  break   
            if valid:
                list1.append(i)
        return list1
