class Solution:
    def countStudents(self, students, sandwiches):
        count = [0, 0]  # count[0] = #students pref 0, count[1] = #students pref 1
        for s in students:
            count[s] += 1

        for sandwich in sandwiches:
            if count[sandwich] == 0:
                break
            count[sandwich] -= 1

        return count[0] + count[1]
