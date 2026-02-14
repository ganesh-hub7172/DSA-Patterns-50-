class Solution:
    def countTestedDevices(self, batteryPercentages):
        used = 0
        for b in batteryPercentages:
            if b - used > 0:
                used += 1
        return used
