class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        count = 0
        
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
                
        return count