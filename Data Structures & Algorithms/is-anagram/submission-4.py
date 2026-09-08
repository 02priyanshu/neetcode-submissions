class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Create a list to track used indices in t
        used_indices = [False] * len(t)
        
        for i in range(len(s)):
            flag = False
            for j in range(len(t)):
                if s[i] == t[j] and not used_indices[j]:
                    flag = True
                    used_indices[j] = True  # Mark this index as used
                    break
            if not flag:
                return False
        
        return True