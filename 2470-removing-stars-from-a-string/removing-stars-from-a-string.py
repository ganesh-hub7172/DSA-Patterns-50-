class Solution:
    def removeStars(self, s):
        st = []
        for c in s:
            if c == '*':
                st.pop()
            else:
                st.append(c)
        return "".join(st)
