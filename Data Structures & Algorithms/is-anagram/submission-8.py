class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}
        for i in range(len(s)):
            if s[i] not in d1.keys():
                d1[s[i]]=0
            else:
                d1[s[i]] = d1[s[i]]+1

        for i in range(len(t)):
            if t[i] not in d2.keys():
                d2[t[i]]=0
            else:
                d2[t[i]] = d2[t[i]]+1

        for i in d1:
            if i not in d2.keys():
                return False
            if d1[i] != d2[i]:
                return False
        return True