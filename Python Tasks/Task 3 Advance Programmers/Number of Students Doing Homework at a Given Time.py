class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        c=0
        for i in range(len(startTime)):
            if(queryTime in range(startTime[i],endTime[i]) or startTime[i]==queryTime or endTime[i]==queryTime):
                c+=1
        return c