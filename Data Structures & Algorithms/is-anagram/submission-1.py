class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s1 = {}
            s2 = {}
            x = 0
            z = 0
            while x < len(s):
                if s[x] in s1:
                    s1[s[x]] += 1
                else:
                    s1[s[x]] = 1
                x += 1
            while z < len(t):
                if t[z] in s2:
                    s2[t[z]] += 1
                else:
                    s2[t[z]] = 1
                z += 1 

            if s1 == s2:
                return True
            else:
                return False

        else:
            return False