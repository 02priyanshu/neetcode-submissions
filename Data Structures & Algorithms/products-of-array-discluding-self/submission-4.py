class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        sufix = [0]*n
        out = [0]*n

        prefix[0] = sufix[n-1] = 1
        for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i-1]
        for j in  range(n-1,0, -1):
            sufix[j-1] = sufix[j]*nums[j]
        for i in range(n):
            out[i] = prefix[i]*sufix[i]
        return out