class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ''' setT = set(t)
        setS = set(s)
        if setS.issubset(setT):
            return True
        else:
            return False
        '''
        if len(s) == 0:
            return True
        charS = 0
        for x in range(0, len(t)):
                if s[charS] == t[x]:
                    charS += 1
                    if charS == len(s):
                        return True
                else:
                    continue
        return False
        
        