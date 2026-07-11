class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        c=0
        for startTime,endTime in zip(startTime,endTime):
            if startTime<=queryTime<=endTime:
                c+=1
        return c

            
