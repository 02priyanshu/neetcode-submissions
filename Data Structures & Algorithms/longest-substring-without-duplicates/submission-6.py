class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_str = ''
        long_str=''
        for i in s:
            if i not in current_str:
                current_str += i
            else:
                if len(current_str)>len(long_str):
                    long_str = current_str
                index=current_str.find(i)
                current_str=current_str[index+1:]+i 
        return max(len(long_str),len(current_str))