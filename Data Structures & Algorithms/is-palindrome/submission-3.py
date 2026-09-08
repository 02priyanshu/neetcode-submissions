class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        nonChar=["?","'",",",".",":"]
        start = 0
        end = len(s)-1
        while(start<=end):
            if s[start] in nonChar or s[start]==" ":
                start+=1
            elif s[end] in nonChar or s[end]==" ":
                end-=1  
            elif s[start] == s[end]:
                start+=1
                end-=1
            else:
                return False
        return True
